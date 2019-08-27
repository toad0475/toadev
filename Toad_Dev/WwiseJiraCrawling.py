import sys
from bs4 import BeautifulSoup
import requests

# 지라이슈 서치 툴
def searchjira(jiranum):
    if jiranum:
        in_jiranum = jiranum
        audiokineticurl = 'https://www.audiokinetic.com'
        quaryurl = 'https://www.audiokinetic.com/search/?term={jira}'.format(jira=in_jiranum)

        with requests.get(quaryurl) as res:
            soup = BeautifulSoup(res.content, 'html.parser')

            if soup.find('div', {'class':'results-details'}):
                if soup.find('div', {'class':'results-details'}).find('a')['href']:
                    url = soup.find('div', {'class':'results-details'}).find('a')['href']

                    #검색결과 중 첫번째 URL 탐색
                    with requests.get(audiokineticurl+url) as res:
                        soup = BeautifulSoup(res.content,'html.parser')
                    
                        
                        if soup.find(name='b', text= in_jiranum):
                            result = soup.find(name='b', text= in_jiranum).findParent()
                            
                            # 결과 출력
                            print(result.get_text().replace('\n','') + '\n')

                        else:
                            print('{} 은/는 {}에서 직접 확인해 보세요.'.format(jiranum, audiokineticurl+url) + '\n')
                else:
                    print('{} 은/는 아직 릴리즈 노트에 업데이트 되지 않았습니다.'.format(jiranum) + '\n')

            else:
                print('{} 은/는 아직 릴리즈 노트에 업데이트 되지 않았습니다.'.format(jiranum) + '\n')
    else:
        print('값이 유효하지 않습니다.' + '\n')

# Jira 이슈 목록 받아서 Loop 실행
if __name__=="__main__":
    print('\n' + '=========== Wwise 지라 이슈 체크 ===========' + '\n')
    for arg in sys.argv[1:]:
        searchjira(arg)
    print(('\n' + '=========== Wwise 지라 이슈 체크 완료 ===========' + '\n'))


# 테스트 용도
# searchjira('WG-34906')
