import os
import requests
import bs4
import re
import datetime
from tqdm import tqdm
import pandas as pd
from urllib.request import urlretrieve
from PyPDF2 import PdfReader

import tensorflow.keras as keras

# 나머지 코드


import tensorflow as tf
from transformers import TFBertForSequenceClassification
from transformers import BertTokenizerFast
from ekonlpy.sentiment import MPKO
from ekonlpy.sentiment import MPCK
import numpy as np
from kss import split_sentences
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration



now = datetime.datetime.now()


url = f'https://finance.naver.com/research/company_list.naver\
?keyword=&brokerCode=&searchType=\
writeDate&writeFromDate={now.isoformat()[0:10]}&writeToDate={now.isoformat()[0:10]}&itemName=&itemCode=&x=0&y=0&page='



def link_parser(url):
    
    page = 1
    next_link_text = "다음"
    link_list = []

    page_url = url + str(page)
    response = requests.get(page_url, headers={'User-Agent': 'Mozill4a/5.0'})
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    last_page = soup.select('table tr td a')[-6]['href'].split('/')[-1].split('=')[-1]

    for _ in tqdm(range(int(last_page))):
        page_url = url + str(page)
        response = requests.get(page_url, headers={'User-Agent': 'Mozill4a/5.0'})
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        link = soup.select('table td:nth-child(2) a')
        for i in range(len(soup.select('table a[target]'))):
            if i < len(link):
                link_list.append('https://finance.naver.com/research/' + link[i]['href'])
        page += 1

    return link_list


def data_parser(link_list):

    stock_name_list = []
    title_list = []
    content_list = []
    target_price_list = []
    opinion_list = []
    broker_list = []
    time_list = []
    view_cnt_list = []
    pdf_link_list = []


    for page_url in tqdm(link_list):

        response = requests.get(page_url, headers={'User-Agent': 'Mozill4a/5.0'})
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        # 종목명
        stock_name = soup.select('th.view_sbj span em')[0].text
        stock_name_list.append(stock_name)

        # 제목
        title = soup.select('th.view_sbj')[0].text.replace('\t', '').strip().split('\n')[1]
        title_list.append(title)

        # 증권사
        broker = soup.select('th.view_sbj')[0].text.replace('\t', '').strip().split('\n')[2].split('|')[0]
        broker_list.append(broker)

        # 업로드 시간
        time = soup.select('th.view_sbj')[0].text.replace('\t', '').strip().split('\n')[2].split('|')[1]
        time_list.append(time)

        # 조회 수
        view_cnt = ''.join(filter(str.isdigit, soup.select('th.view_sbj')[0].text.replace('\t', '').strip().split('\n')[2].split('|')[2]))
        view_cnt_list.append(view_cnt)

        # 내용
        content = ':'.join([i.text for i in soup.select('table div font')])
        content_list.append(content)  
        try:
            # 목표가
            target_price = soup.select('em.money > strong')[0].text.replace(',', '')
            target_price_list.append(target_price)

            # 의견
            opinion = soup.select('em.coment')[0].text
            opinion_list.append(opinion)
        except:
            target_price_list.append(-9999)
            opinion_list.append('no_opinion')

        try:
            # 리포트 링크
            pdf_link = soup.select('table td div a')[0]['href']
            pdf_link_list.append(pdf_link)
        except:
            pdf_link_list.append('no_pdf')
    
    df = pd.DataFrame({'종목명' : stock_name_list,
                '제목' : title_list,
                '내용' : content_list,
                '증권사' : broker_list,
                '날짜' : time_list,
                '조회수' : view_cnt_list,
                '목표가' : target_price_list,
                '의견' : opinion_list,
                '리포트링크' : pdf_link_list})
    
    df['pdf이름'] = df['종목명'] + '_' + df['증권사'] + '_' + df['날짜']
    df.drop_duplicates(subset='pdf이름', inplace=True)
    df = df[df['리포트링크'].notnull()]
    df.sort_values(by=['pdf이름'], inplace = True)
    df.reset_index(inplace = True)
    df.drop(['index'], axis = 1, inplace = True)
    
    return df



def pdf_download(df):
    pdf_link = df['리포트링크'].to_list()
    pdf_name = df['pdf이름'].to_list()
    
    directory = f'/Users/sunghyunkim/Desktop/Final_Project/{now.isoformat()[0:10]}_pdf/'
    
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    for i, name in zip(pdf_link, pdf_name):
        pdf_path = os.path.join(directory, f'{name}.pdf')
        if not os.path.exists(pdf_path):
            response = requests.get(i, stream=True, verify=False)
            with open(pdf_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
    
    return df

def pdf_text_parsing(df):
    
    path = f'/Users/sunghyunkim/Desktop/Final_Project/{now.isoformat()[0:10]}_pdf/'
    pdf_list = os.listdir(path)
    text_list = []

    for i in tqdm(pdf_list):
        try:
            pdf = PdfReader(path + i, 'rb')
            text = pdf.pages[0].extract_text() + pdf.pages[1].extract_text()
            text_list.append(text)
        except:
            text_list.append('error')
    
    df['텍스트'] = text_list
    
    
    def apply_regex(text):
        pattern = r'[^\w가-힣\s.\x20-\x7E]'
        matches = re.sub(pattern, '',text)
        return ''.join(matches)
    
    def has_indian_language(text):
        pattern = re.compile("[\u0900-\u097F\u0A00-\u0A7F]")  # 힌디어 및 펀자브어 유니코드 범위
        return bool(re.search(pattern, text))
    
    df['텍스트'] = df['텍스트'].apply(apply_regex)
    df['인코딩'] = df['텍스트'].apply(lambda x: has_indian_language(x))
    
    df = df[df['인코딩'] == False]
    df.drop(['인코딩'], axis = 1, inplace = True)
    
    return df


""" 
---------------------------------------------------------------------
여기서부터 감성점수, 감성토픽, 요약문 생성 로직
---------------------------------------------------------------------
"""


def sentiment_score_func(df):
    tf.config.run_functions_eagerly(True)

    df['텍스트'] = df['텍스트'].apply(lambda x: re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣a-zA-Z.\s]', '', x))
    df['텍스트'] = df['텍스트'].apply(lambda x: re.sub('\n', '', x))
    df['텍스트'] = df['텍스트'].apply(lambda x: ".." if x.strip() == "" else x)
    

    model = TFBertForSequenceClassification.from_pretrained("klue/bert-base", num_labels=3, from_pt=True)
    optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
    model.compile(optimizer=optimizer, loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])
    mpko = MPKO(kind=1)
    mpck = MPCK()

    sent_score_list = []
    sent_tokens_list = []
    
    def modify_text_list(text_list):
        modified_list = []
        for text in text_list:
            modified_text = re.sub('/[A-Z]+', '', text)  # 대문자 알파벳과 슬래시(/)를 제거합니다.
            modified_text = modified_text.replace(';', '')
            modified_list.append(modified_text)
        return modified_list


    for i in tqdm(range(len(df))):
        text = split_sentences(df['텍스트'].iloc[i], backend='punct')
        tokenizer = BertTokenizerFast.from_pretrained("klue/bert-base")
        text = tokenizer(text, truncation = True, padding = True, return_tensors='tf')
        pred = model.predict(text)

        pred_list = []
        for j in range(len(pred.logits)):
            pred_list.append(np.argmax(tf.nn.softmax(pred.logits, axis=0)[j]))

        bert_list = [num if num != 2 else -1 for num in pred_list]
        bert_sent = sum(bert_list) / len(bert_list)


        mpko_tokens = mpko.tokenize(df['텍스트'].iloc[i])
        mpko_dict = mpko.get_score(mpko_tokens)
        mpko_score = mpko_dict['Polarity']

        mpck_tokens = mpck.tokenize(df['텍스트'].iloc[i])
        mpck_ngrams = mpck.ngramize(mpck_tokens)
        mpck_dict = mpck.classify(mpck_ngrams, intensity_cutoff = 1)
        mpck_score = mpck_dict["Polarity"]
        
        tokens_list = modify_text_list(mpck_ngrams)
        sent_tokens_list.append(tokens_list)

        sent_score = ((bert_sent * 0.25) + mpko_score + mpck_score) / 3
        sent_score_list.append(sent_score)
        
    df['감성점수'] = sent_score_list
    df['감성토픽'] = sent_tokens_list
    
    return df

def text_summerize(df):
    
    tokenizer = PreTrainedTokenizerFast.from_pretrained("ainize/kobart-news")
    model = BartForConditionalGeneration.from_pretrained("ainize/kobart-news")
    summerize_list = []
    
    for i in tqdm(df.index):

        text = df['텍스트'][i]
        inputs = tokenizer.encode_plus(text, truncation=True, padding='longest', max_length=512, return_tensors='pt')
        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask

        summary_text_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            bos_token_id=model.config.bos_token_id,
            eos_token_id=model.config.eos_token_id,
            length_penalty=1.3,
            max_length=128,
            min_length=16,
            num_beams=4
        )

        sum_text = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True).replace('.', '')

        summerize_list.append(sum_text)

    df['요약문'] = summerize_list
    
    return df

def last_squence(df):
    df['요약문'].replace('', np.nan, inplace=True)
    df['요약문'].fillna('요약문없음', inplace=True)
    df.to_csv('pdf_text_last.csv')
    return


if __name__ == '__main__':
        
    link_list = link_parser(url)
    print('증권 데이터 링크 크롤링 완료')
    df_report_link = data_parser(link_list)
    print('데이터 파싱 완료')
    df = pdf_download(df_report_link)
    print('PDF 다운로드 완료')
    pdf_text_list = pdf_text_parsing(df)
    print('유효한 PDF df 생성')
    df_score_topic = sentiment_score_func(pdf_text_list)
    print('감성점수, 감성토픽 컬럼 추가')
    summrized_df = text_summerize(df_score_topic)
    last_squence(summrized_df)
    print('요약문 컬럼 추가')
    print('DB용 CSV 저장완료, JSON 파일 생성 완료')
