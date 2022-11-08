# 다른 .py 파일 import
from Get_news_items import Get_news_items
from Save_data_mysql import Save_data_mysql
from Save_data_csv import Save_data_csv

if __name__ == "__main__":
    # # 네이버 뉴스 검색 url 
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%B9%98%EB%A7%A4%2B%EC%9D%B8%EC%A7%80&sort=0&photo=3&field=0&pd=0&ds=&de=&cluster_rank=11&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=' 
    max_idx = 10 # 10개의 기사를 가져옴

    title_list, date_list, content_list, url_list = Get_news_items(url, max_idx)    # 기사 정보 가져오기

    # Save_data_mysql(title_list, date_list, content_list, url_list)    # MySQL에 저장

    Save_data_csv(title_list, date_list, content_list, url_list)    # CSV 파일로 저장