import sys
from pprint import pprint
from libs.kh_parser import get_mp3_links
from libs.url_file_download import save_file_from_url


def print_bar(length, current):
    # normalize to % and scaled to 50 chars
    normal = (current * 50) // length
    done = '#' * normal
    todo = '=' * (50-normal)
    bar = "(%03d/%03d)[%s%s]" % (current, length, done, todo)
    print(bar)


def main(site_url):
    all_files = get_mp3_links(site_url)
    length = len(all_files)
    step = 100/length
    print_bar(length, 0)
    for i, link in enumerate(all_files):
        save_file_from_url(link[0], link[1])
        print_bar(length, i+1)
    print('Done!')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        site_url = sys.argv[1]
        main(site_url)
    else:
        print('ERROR: Needs album url \n python khdownloader.py <site_url>')
