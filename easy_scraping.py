from icrawler.builtin import GoogleImageCrawler as GIC

crawler = GIC(storage={"root_dir": "TOILET"})
crawler.crawl(keyword="トイレ", max_num=200)
