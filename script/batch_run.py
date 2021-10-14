import sys

from sotag.download.sotag_downloader import SOTagDownloader


def run_batch(sta: int, end: int):
    save_name = "../data/run_{}_{}.bin".format(sta, end)
    searcher = SOTagDownloader()
    batch_tag_dict = {k: searcher.tag_dict[k] for k in list(searcher.tag_dict)[sta:end]}
    for tag in batch_tag_dict.keys():
        print(tag)
        item = searcher.get_tag_item_for_one_tag(tag)
        searcher.so_tag_item_collection.add_so_tag_item(item)
    searcher.save(save_name)


if __name__ == "__main__":
    sta = int(sys.argv[1])
    end = int(sys.argv[2])
    run_batch(sta=sta, end=end)
    # ThinkPad-X270:~/lab/sotag$ python batch_run.py 0 5
    #   这样就能开多个终端分批跑
