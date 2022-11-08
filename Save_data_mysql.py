import pymysql

def Save_data_mysql(title_list, date_list, content_list, url_list):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000', db='project_Dementia', charset='utf8') #SQL 연동
    cursor = db.cursor()    # 커서 생성

    # 데이터 저장
    for i in range(len(title_list)):    
        sql = "INSERT INTO naver_news VALUES("+ str(i+1) +",'" + title_list[i] + "', " + date_list[i] + ", '" + content_list[i] + "', '" + url_list[i] + "');"
        cursor.execute(sql) # SQL 실행
        print("====================================="+str(i)+"=====================================")
    
    db.commit() # 데이터베이스에 반영
    db.close()  # DB 연결 종료
    