import pandas as pd
import psycopg2
from datetime import date

def dbcommit():
    
    # CSV 파일 경로
    csv_file_path = 'pdf_text_last.csv'

    # CSV 파일 읽기
    data = pd.read_csv(csv_file_path, index_col=0)


    # PostgreSQL 데이터베이스 연결 설정
    conn = psycopg2.connect(
        host='localhost',    # 호스트 이름
        port=5432,           # 포트 번호 (기본값: 5432)
        user='postgres',     # 사용자 이름
        password='password', # 비밀번호
        database='report',   # 데이터베이스 이름
    )

    # 데이터베이스에 데이터 쓰기
    cursor = conn.cursor()

    table_name = 'stock_broker_report'  # 실제 테이블 이름으로 수정 필요

    try:
        today = date.today().strftime("%Y-%m-%d")
        for index, row in data.iterrows():
            pdf_name = row['pdf이름']
            select_query = f'SELECT pdf_name FROM {table_name} WHERE pdf_name = %s AND wdate = %s'
            cursor.execute(select_query, (pdf_name, today))
            result = cursor.fetchone()
            if result is None:
                insert_query = """
                INSERT INTO {} (pdf_name, 
                                wdate, 
                                company,
                                title,
                                content,
                                stock_broker,
                                target_opinion,
                                target_price,
                                report_link,
                                pdf_text,
                                pdf_summarize,
                                pdf_sent_score,
                                pdf_sent_topic) 
                VALUES (%s, %s, 
                        %s, %s,
                        %s, %s,
                        %s, %s,
                        %s, %s,
                        %s, %s,
                        %s)
                """.format(table_name)

                values = (row['pdf이름'], row['날짜'], 
                        row['종목명'], row['제목'],
                        row['내용'], row['증권사'],
                        row['의견'], row['목표가'],
                        row['리포트링크'], row['텍스트'],
                        row['요약문'], row['감성점수'],
                        row['감성토픽'])  # 열 이름 수정 필요

                cursor.execute(insert_query, values)
                conn.commit()
    except Exception as e:
        print('에러가 발생했습니다:', e)

    finally:
        # 연결 종료
        cursor.close()
        conn.close()
    
    return

if __name__ == '__main__':
    print('DB 저장 시작')
    dbcommit()
    print('DB 저장 완료')
