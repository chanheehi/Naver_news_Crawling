from datetime import datetime
import csv

def Save_data_csv(title_list, date_list, content_list, url_list):
    filename = datetime.now().strftime('./result/%Y-%m-%d_%H시%M분-%S초.csv')

    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'date', 'content', 'url'])
        for i in range(len(title_list)):
            writer.writerow([title_list[i], date_list[i], content_list[i], url_list[i]])
            print("====================================="+str(i)+"=====================================")
    f.close()