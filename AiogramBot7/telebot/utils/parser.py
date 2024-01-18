import requests
import fake_useragent
from bs4 import BeautifulSoup


def main():
    # agent = fake_useragent.UserAgent().random
    header = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,id;q=0.6,zh-TW;q=0.5,zh;q=0.4,fr;q=0.3,bg;q=0.2",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-aidata-fp": "r7pGVwZMo6yW3vyTHgXZtw",
        "x-alt-referer": "",
        "x-first-party-cookie": "26a4482469316ca38e4061cd23722315",
        "cookie": "uuid=027ebc98-7ccb-4767-66a1-eb80bfd4ef0d; cookiesyncs=000000000000000000000000dd1d48a5fd31177db6c2feeab8f237b4069093d320917cef2ea11b1ff17cec694bb875a0efb567b0d73f92c927ec03fe32423d785c095f4e02890fc969adaf15820942ed445153c38fc9516e94b4b850df1d0efdf896fc710f51d6ed1ee5c8f4ebd68929b4b5974f64a750c47bce724c6153ba19b5368f8c083b1e149e426a99977df6245697f339308c892b56f74bbf23b34732cb24a7e7e3fd1c408db9660e47f379a93b72a2401db97f0ba243b9dd0ef55f905f6c4fb04314bac4a70e6ff37c50e0e01987f4279d5ec7196273a25531be9734a7a43c987f72680c4e2f96f05afcd1854683aa079afc08097c6934bf0c056522b6e70ab1037da4e821e9ede318e5bd387fca3878a647b5c13c17df60e9009d91b01fe9ced3628022c1b0429524edbd3779b3368c4266f5ab10bd1f0ce7cf80731090f3fdb26f0b2d4d3dde7d25f4e879147d12cb1ecb501696d51f097ba96a57ffa3698ed09ce37dabe5c0dc29e21c9fa77f11300a38bb7cbd1fa14729c5ec49a54d354cff51379d7b3855a87e3b7746fd5175adeecedab059958fb35d2da850dbbfe9018d11c20277c583cf3ff266b2ed015d2f24bc0a6df0ba0d355440393b48d3dbd3e80dbea56f1a1f94bdbc814a4172ed02bf37e772ac6071ebccbd4ffdcdf7260b318dfdfd4296a085b97e079ee15017979cae8e94071ae826a21da15fac549ffe39ebbd41e401e4bc96b9713587d5ab5c2379d913e56d710db7adc10bc75584fd8b2918b134db32f218acff8df80fb04cef83d94794c69feac6ef60ed1daeacef3c2da179a505b918b80ce19f3120f8e1fdc7b351cf6d387fdf06c0bee280241b4495e3492d6bbc32db32e7b6cec855c6d4cc75be832c517f35815c90aa4eeebb9155bb6e9d8222b716a918b06fc9c8a3a360e3d9ab65c3a5f1cb72ec84cd361f9adce3e4698febec4bd0649b61349ce7c210a6999f544323093e5e62d974d145ced966e9397fef8f594d5be2f96a62da8f3927193e5cb2113235f4c16ada15aaa0dc78744e02a8c44178bd41153afb5145da3543e3ce2cdc8f606e6515cac31ee9c28ce38078248dceb572fcc696cc29ca8b4d5558e85039c1ad4a52fa4f4f656c3e0035e4b8272dd6bc6e4035ac84b9e74701c37b3c982ae3102040b9dfa32bd2daf991b4b3f249ea94c704ee7a81f29a1a206cc921d80fc568ea65b479f2ae2fe8f8ce884cca21bb8da3d3c6a9ce41cdcbc86b42e6a32330618a01417376b780ed46feece76e5fba8faf815d34b2a0e8396aba787ed6d78b9cd827891da3f50b2b19c4d37c370ad3094936864a1abbcbbf098f43a395c97b8e74bdb0e6e406d6bbfe91c2782fc3bc2e44d4ff5f04912e13ec3fdd27574120fbea6cf8cdc40f05b4d0d6acc43e24c8f8ce9ffa7ac459fcd5716201bcb980d1a276bcdce117d1b244f02a8c5fbff6097e030976fcb286087a28881d148404ce1c",
        "Referer": "https://tube.buzzoola.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    # link = "https://www.avito.ru/all/telefony/mobilnye_telefony/apple/iphone_13_pro_max/512_gb-ASgBAgICBESywA3yvcgBtMANzqs5sMENiPw35uAN~sFc?cd=1&f=ASgBAgECBESywA3yvcgBtMANzqs5sMENiPw35uAN~sFcAUXGmgwaeyJmcm9tIjo1MDAwMCwidG8iOjUwMDAwMH0"
    link = r'c:\!SAVE\parsing\index.html'
    response = requests.get(link, headers=header).text

    soup = BeautifulSoup(response, "lxml")
    print(soup)
    # block = soup.find('div', {"data-marker": "item"})
    catalog = soup.find('div', {'data-marker': 'catalog-serp'})
    print(catalog)
    # block2 = block.find('h3', class_="styles-module-root-TWVKW").text
    # block3 = block.find('strong', class_="styles-module-root-LIAav").text
    # block4 = block.find('p', class_="styles-module-size_s-awPvv").text
    #
    # print(block2)
    # print(block3)
    # print(block4)


if __name__ == '__main__':
    main()
