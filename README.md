# sscrape

I used [playwright](https://playwright.dev/python/docs/api/class-playwright#playwright-chromium) for headless browser, and used header spoofing, to prevent websites with browser fingerprinting.

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
python3 scrape
```