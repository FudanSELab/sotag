import csv
from unittest import TestCase
from path import ROOT_PATH
from sotag.download.sotag_downloader import SOTagDownloader
from sotag.models.tag import SOTagItem


class TestSoTagSearcher(TestCase):

    def test_so_tag_searcher(self):
        # 此函数用于测试是否能从网爬取某个tag的全部SOTagItem类型中定义的数据，参数是一个tag字符串
        searcher = SOTagDownloader()
        # print(len(searcher.synonyms_data))
        # self.assertTrue(len(searcher.synonyms_data) > 0)
        item: SOTagItem = searcher.get_tag_item_for_one_tag("python")
        print(item.tag_name)
        print(item.get_tag_id())
        print(item.get_tag_count())
        print(item.get_excerpt_post_id())
        print(item.get_wiki_post_id())
        print('_______________________________________short________________________________________')
        print(item.get_short_description())
        print('_______________________________________long________________________________________')
        print(item.get_long_description())
        print('_______________________________________synonyms________________________________________')
        print(item.get_tag_synonyms())
        print('_______________________________________html________________________________________')
        print(item.get_info_html())
        # self.assertIsNotNone(item)
        # searcher.run() # todo make run() has a testable way, not run for all tags.
        # searcher.save("test.bin")

    def test_show_one_tag_in_collection(self):
        # 此函数用于测试 在本地的某个bin中 是否有 某个tag的全部SOTagItem类型中定义的数据 ，参数是一个地址 和一个tag字符串
        searcher = SOTagDownloader(so_tag_item_collection_path="/{}/data/run_100_10000.bin".format(ROOT_PATH))
        item: SOTagItem = searcher.so_tag_item_collection.get_so_tag_item('compiz')
        # return item
        print(item.tag_name)
        print(item.get_tag_id())
        print(item.get_tag_count())
        print(item.get_excerpt_post_id())
        print(item.get_wiki_post_id())
        print('_______________________________________short________________________________________')
        print(item.get_short_description())
        print('_______________________________________long________________________________________')
        print(item.get_long_description())
        print('_______________________________________synonyms________________________________________')
        print(item.get_tag_synonyms())
        print('_______________________________________html________________________________________')
        print(item.get_info_html())

    def test_bin_tag_items_to_csv(self):
        # 此函数用于将 本地某个bin中的数据 格式化保存到 本地csv，方便测试查看，一般不用
        searcher = SOTagDownloader(so_tag_item_collection_path="../../data/so_tag_info2.bin")
        collection = searcher.so_tag_item_collection
        with open('test2.csv', 'a+', newline='\n') as file:
            csv_file = csv.writer(file)
            for tag in collection.name2sotag.keys():
                item: SOTagItem = collection.get_so_tag_item(tag)
                data1 = {'tag_name': item.get_tag_name(),
                         'id': item.get_tag_id(),
                         'count': item.get_tag_count(),
                         'excerpt_post_id': item.get_excerpt_post_id(),
                         'wiki_post_id': item.get_wiki_post_id(),
                         'short_description': item.get_short_description(),
                         'long_description': item.long_description,
                         'info_html': item.get_info_html()
                         }
                data2 = data1.values()
                csv_file.writerow(data2)

    def test_run_batch(self, sta: int, end: int):
        searcher = SOTagDownloader()
        batch_tag_dict = {k: searcher.tag_dict[k] for k in list(searcher.tag_dict)[sta:end]}
        for tag in batch_tag_dict.keys():
            item = searcher.get_tag_item_for_one_tag(tag)
            searcher.so_tag_item_collection.add_so_tag_item(item)
        save_name = "run_{}_{}.bin".format(sta, end)
        searcher.save(save_name)
