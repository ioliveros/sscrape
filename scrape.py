import sys
import argparse
import logging
import random
import string

from datetime import datetime, timedelta
import uuid
import json
import traceback
from urllib.parse import urlparse

import playwright
from playwright.sync_api import sync_playwright
from lxml import html


logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("playwright.log"),
        logging.StreamHandler()
    ]
)
    
logger = logging.getLogger('playwright')


def get_root_domain(url):
    parsed_url = urlparse(url)
    return f'{parsed_url.scheme}://{parsed_url.netloc}'

def random_string(length=10):
    """Generate a random alphanumeric string."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_date(start_year=2020, end_year=2025):
    """Generate a random date in ISO format."""
    start_date = datetime(year=start_year, month=1, day=1)
    end_date = datetime(year=end_year, month=12, day=31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.isoformat()

def generate_cookie():
    return f"""audience=audiences=; rfx-forex-rate=currencyCode=PHP&exchangeRate={random.uniform(50, 70):.4f}&quoteId={random.randint(10000000, 99999999)}; internationalshippref=preferredcountry=PH&preferredcurrency=PHP&preferredcountryname=Philippines; no-track=ccpa={random.choice(['true', 'false'])}; nordstrom=bagcount={random.randint(0, 10)}&firstname={random_string(5)}&ispinned={random.choice(['True', 'False'])}&isSocial={random.choice(['True', 'False'])}&shopperattr=||{random.randint(0, 10)}|{random.choice(['True', 'False'])}|-1&shopperid={uuid.uuid4()}&USERNAME={random_string(8)}; nui=firstVisit={random_date()}&geoLocation=&isModified={random.choice(['true', 'false'])}&lme={random.choice(['true', 'false'])}; usersession=CookieDomain=nordstrom.com&SessionId={uuid.uuid4()}; experiments=ExperimentId={uuid.uuid4()}; wlcme={random.choice(['true', 'false'])}; ftr_blst_1h={random.randint(1000000000000, 2000000000000)}; storemode=version={random.randint(1, 10)}&postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive={random.randint(0, 1)}&; storeeligiblepromise=eligiblePromises=; _gcl_au=1.1.{random.randint(10000000, 99999999)}.{random.randint(10000000, 99999999)}; n.com_shopperId={uuid.uuid4()}; _ga=GA1.1.{random.randint(100000000, 999999999)}.{random.randint(100000000, 999999999)}; __gads=ID={uuid.uuid4()}:T={random.randint(1000000000, 2000000000)}:RT={random.randint(1000000000, 2000000000)}:S=ALNI_Mbna7u2g-Ox_ygVVbRQGvtF5mlmRQ; __eoi=ID={uuid.uuid4()}:T={random.randint(1000000000, 2000000000)}:RT={random.randint(1000000000, 2000000000)}:S=AA-AfjaGZ6TYJD-EVc1VvJXrR_HY; bc_invalidateUrlCache_targeting={random.randint(1000000000000, 2000000000000)}; IR_gbd=nordstrom.com; _fbp=fb.1.{random.randint(1000000000, 2000000000)}.{random.randint(1000000000, 2000000000)}; _tt_enable_cookie={random.randint(0, 1)}; _ttp={random_string(24)}; bluecoreNV={random.choice(['true', 'false'])}; _pin_unauth={random_string(36)}; FPLC={random_string(36)}; __podscribe_nordstrom_referrer=https://duckduckgo.com/; __podscribe_nordstrom_landing_url=https://www.nordstrom.com/; __podscribe_did=pscrb_{uuid.uuid4()}; Ad34bsY56={random_string(36)}; trx={random.randint(1000000000000000000, 9999999999999999999)}; mdLogger={random.choice(['true', 'false'])}; kampyle_userid={uuid.uuid4()}; client=viewport={random.choice(['1_SMALL', '2_SMALL', '2_LARGE'])}; shoppertoken=shopperToken={uuid.uuid4()}"""

def random_user_agent():
    browsers = {
        'Chrome': [f'88.0.{random.randint(4000, 4999)}.{random.randint(100, 199)}', 
                   f'92.0.{random.randint(4000, 4999)}.{random.randint(100, 199)}'],
        'Firefox': [f'89.0.{random.randint(0, 10)}', 
                    f'95.0.{random.randint(0, 10)}'],
        'Safari': [f'14.{random.randint(0, 2)}.{random.randint(0, 10)}', 
                   f'15.{random.randint(0, 2)}.{random.randint(0, 10)}'],
        'Edge': [f'91.0.{random.randint(1000, 1999)}.{random.randint(0, 99)}', 
                 f'94.0.{random.randint(1000, 1999)}.{random.randint(0, 99)}']
    }
    os_list = [
        'Windows NT 10.0; Win64; x64',
        'Windows NT 10.0; Win32',
        'Macintosh; Intel Mac OS X 10_15_7',
        'Macintosh; Intel Mac OS X 10_14_6',
        'X11; Ubuntu; Linux x86_64',
        'X11; Debian; Linux x86_64'
    ]
    browser = random.choice(list(browsers.keys()))
    version = random.choice(browsers[browser])
    os = random.choice(os_list)

    # Generate User-Agent string
    if browser == 'Chrome':
        user_agent = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36"
    elif browser == 'Firefox':
        user_agent = f"Mozilla/5.0 ({os}; rv:{version}) Gecko/20100101 Firefox/{version}"
    elif browser == 'Safari':
        user_agent = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{version} Safari/537.36"
    elif browser == 'Edge':
        user_agent = f"Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 Edg/{version}"

    return user_agent

def scrape(url, proxy):
    with sync_playwright() as p:
        cookie = generate_cookie()
        user_agent = random_user_agent()
        headers = {
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Cookie": cookie 
        }
        logger.info(json.dumps(headers, indent=2))
        browser = p.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-gpu"], 
            proxy={"server": f"http://{proxy}"}
        )

        logger.info(f"go to page:: {url}")
        
        page = browser.new_page()
        page.set_extra_http_headers(headers)
        page.goto(url, wait_until="load")
        page.wait_for_load_state("networkidle")

        html_content = page.content()

        # look for product links
        has_links = save_data(url, html_content, proxy) 

        # save page for verification
        if has_links:
            save_page(proxy, html_content) 
        
        browser.close()

def get_product_links(url, html_content, proxy):

    xpath_expression = '//*[@id="product-results-view"]/div/div/div/section/div/article/a/@href'
    tree = html.fromstring(html_content)
    result = tree.xpath(xpath_expression)

    root_domain = get_root_domain(url)
    links = []
    for link in result:
        links.append(f'{root_domain}{link}')
    
    logger.info(f'found links:: {len(links)}')
    if len(links) > 0:
        with open(f'products/product-links::{proxy}.json', 'w') as f:
            f.write(json.dumps(links, indent=2))

    return links

def save_data(url, html_content, proxy):
    product_links = get_product_links(url, html_content, proxy)
    return True if len(product_links) > 0 else False

def save_page(proxy, html_content):
    file_name = f"page-{proxy}.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)
    logger.info(f"Successfully sraped:: {file_name}")

def run(url, proxy_file):

    proxy_list = []
    with open(proxy_file, "r") as f:
        for _ in f.read().split("\n"):
            item = _.strip()
            if not item: continue
            proxy_list.append(item)

    for proxy in proxy_list:
        try:
            logger.info(f"using proxy:: {proxy}")
            scrape(url, proxy)
        except playwright._impl._errors.Error:
            logger.warning(f'failed using:: {proxy}')
        except:
            logger.error(f"failed using:: {proxy} - trace: {traceback.format_exc()}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run web scraping with proxies.")
    parser.add_argument("url", help="The URL to scrape.")
    parser.add_argument("proxy_file", help="The file containing proxy list.")
    
    args = parser.parse_args()
    run(args.url, args.proxy_file)