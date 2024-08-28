# sscrape

I used [playwright](https://playwright.dev/python/docs/api/class-playwright#playwright-chromium) for headless browser, and used header spoofing to avoid websites with browser fingerprinting anti-bot blockers.

### install dependencies
```sh
python3 -m venv env
(env) pip3 install -r requirement.txt
```

I don't buy proxies, so I resorted to use free proxies from the internet, here's the sources I used

```
https://free-proxy-list.net/
https://spys.me/proxy.txt
https://spys.one/en/
https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt
```

How to run?
```bash
python3 sscrape.py \
    --url="https://www.nordstrom.com/browse/women/clothing/dresses" \
    --proxy_file="proxies.txt"
```

output
```bash
❯ ./run.sh
2024-08-28 22:00:07,425 - playwright - INFO - using proxy:: 157.100.60.170:999
2024-08-28 22:00:07,425 - asyncio - DEBUG - Using selector: KqueueSelector
2024-08-28 22:00:06,613 - playwright - INFO - {
  "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.1963.76 Safari/537.36 Edg/91.0.1963.76",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Cookie": "audience=audiences=; rfx-forex-rate=currencyCode=PHP&exchangeRate=69.2011&quoteId=22671597; internationalshippref=preferredcountry=PH&preferredcurrency=PHP&preferredcountryname=Philippines; no-track=ccpa=true; nordstrom=bagcount=9&firstname=9wqw8&ispinned=False&isSocial=False&shopperattr=||5|False|-1&shopperid=17c34767-131e-49f7-b436-748a96842e42&USERNAME=NWLO6u3a; nui=firstVisit=2022-09-12T00:00:00&geoLocation=&isModified=false&lme=false; usersession=CookieDomain=nordstrom.com&SessionId=4f3b44c8-79df-4665-ab33-c0a56f007cbc; experiments=ExperimentId=c4c7220e-f3e8-4d64-9282-17ff77679886; wlcme=false; ftr_blst_1h=1067700379673; storemode=version=4&postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0&; storeeligiblepromise=eligiblePromises=; _gcl_au=1.1.91690840.39484993; n.com_shopperId=8e9738d1-207a-4ed8-8acf-47af29400c22; _ga=GA1.1.298359232.769616001; __gads=ID=fef32f6a-6a0b-4cc7-b30a-d02f2bd2393c:T=1675957446:RT=1847538001:S=ALNI_Mbna7u2g-Ox_ygVVbRQGvtF5mlmRQ; __eoi=ID=74698536-697d-474c-b985-68d9be714169:T=1800666334:RT=1707642268:S=AA-AfjaGZ6TYJD-EVc1VvJXrR_HY; bc_invalidateUrlCache_targeting=1183316126162; IR_gbd=nordstrom.com; _fbp=fb.1.1901294080.1582576026; _tt_enable_cookie=1; _ttp=M2nfL2DKLYjCbKibH7nfwwRA; bluecoreNV=false; _pin_unauth=2ST1Vnfx0LxXR5W8eykbHqyH8VWxDlGH9aOi; FPLC=Sbgc9rLkspJkxVvzzafkhN30rvqN0pcLHO9d; __podscribe_nordstrom_referrer=https://duckduckgo.com/; __podscribe_nordstrom_landing_url=https://www.nordstrom.com/; __podscribe_did=pscrb_2344f7ae-e5f7-4ce4-8374-924ba36a9f2f; Ad34bsY56=5lIjKSVk0PamUfNA2iEgPZjafJ04wkgMm8BU; trx=9889709198773017800; mdLogger=false; kampyle_userid=954575a4-5bbc-40ea-8abf-9d574ccb4668; client=viewport=2_LARGE; shoppertoken=shopperToken=77135b5e-bd78-4b34-9359-dac0d0718a95"
}
2024-08-28 22:00:07,427 - playwright - INFO - found links:: 62
2024-08-28 22:00:07,430 - playwright - INFO - Successfully sraped:: page-20.204.212.76:3129.html
```