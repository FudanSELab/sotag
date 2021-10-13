import sys

from sotag.download.sotag_downloader import SOTagDownloader
from sotag.models.tag import SOTagItem


def rerun_batch(sta: int, end: int):
    save_name = "../data/run_{}_{}.bin".format(sta, end)
    searcher = SOTagDownloader(save_name)
    batch_tag_dict = {k: searcher.tag_dict[k] for k in list(searcher.tag_dict)[sta:end]}
    num = 0
    for tag in batch_tag_dict.keys():
        item: SOTagItem = searcher.so_tag_item_collection.get_so_tag_item(tag)
        if item.get_short_description() == "" or item.get_long_description() == "":
            print(tag)
            num = num + 1
            item = searcher.get_tag_item_for_one_tag(tag)
            searcher.so_tag_item_collection.add_so_tag_item(item)
        else:
            print("{} is ok ~~ ".format(tag))
    if num == 0:
        print("not need rerun any more  ~~~")
    else:
        print("this rerun get {} tags".format(num))
        searcher.save(save_name)

if __name__ == "__main__":
    sta = int(sys.argv[1])
    end = int(sys.argv[2])
    rerun_batch(sta=sta, end=end)
    # ThinkPad-X270:~/lab/sotag$ python batch_run.py 0 5
    #   这样就能开多个终端分批跑
