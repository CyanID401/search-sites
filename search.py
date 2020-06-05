import webbrowser
import time


def get_links(keyword):
    bw = 'https://bookwalker.jp/search/?qcat=&word=' + keyword
    ejp = 'https://ebookjapan.yahoo.co.jp/search?keyword=' + keyword
    ajp = 'https://www.amazon.co.jp/s?k=' + keyword
    md = 'https://mangadex.org/quick_search/' + keyword
    mu = 'https://www.mangaupdates.com/series.html?search=' + keyword
    mal = 'https://myanimelist.net/manga.php?q=' + keyword
    rjd = 'http://www.romajidesu.com/dictionary/meaning-of-{}.html'.format(keyword)
    jisho = 'https://jisho.org/search/' + keyword
    gt = 'https://translate.google.com/#view=home&op=translate&sl=ja&tl=en&text=' + keyword
    nat = 'https://natalie.mu/search?query={}&g=comic'.format(keyword)
    ann = 'https://www.animenewsnetwork.com/search?q=' + keyword
    links_list = [bw, ejp, ajp,
                  md, mu, mal,
                  rjd, jisho, gt,
                  nat, ann]
    return links_list


if __name__ == '__main__':
    kwrd = input('Input keyword to search for: ')
    links = get_links(kwrd)
    for i in range(len(links)):
        print(links[i])
        webbrowser.open(links[i])
        time.sleep(0.2)
