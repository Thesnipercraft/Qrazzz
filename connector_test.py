from connector import UrlQueue
from connector import DataStore

url_queue = UrlQueue(host="host", user="user", password="pass", database="database")
data_store = DataStore(host="host", user="user", password="pass", database="database")
url_queue.add_url("https://example.com/1")
url_queue.add_url("https://example.com/2")
url_queue.add_url("https://example.com/3")


id = url_queue.get_id()
print(id)
url = url_queue.get_url(id)
print(url)
url_queue.delete_url(id)



data_store.add_data("https://example.com/", "example, domain, illustrative")
data_store.add_data("https://example.com/1", "example, domain, illustrative")

'''data_store.delete_data(id)'''