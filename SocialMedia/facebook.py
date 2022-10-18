import requests

class Facebook:
    def postHalfTimeScore(self):
        fHN = open("output/homeTeamName.txt", "r")
        homeTeamName = fHN.read()
        fHS = open("output/homeTeamScore.txt", "r")
        homeTeamScore = fHS.read()
        fAN = open("output/awayTeamName.txt", "r")
        awayTeamName = fAN.read()
        fAS = open("output/awayTeamScore.txt", "r")
        awayTeamScore = fAS.read()

        msg = 'It is half time of action with a score of ' + homeTeamScore + " for " + homeTeamName + " and " + awayTeamScore + " for " + awayTeamName + "."

        self.post(msg)

        fHN.close()
        fHS.close()
        fAN.close()
        fAS.close()

    def postFullTimeScore(self):
        fHN = open("output/homeTeamName.txt", "r")
        homeTeamName = fHN.read()
        fHS = open("output/homeTeamScore.txt", "r")
        homeTeamScore = fHS.read()
        fAN = open("output/awayTeamName.txt", "r")
        awayTeamName = fAN.read()
        fAS = open("output/awayTeamScore.txt", "r")
        awayTeamScore = fAS.read()

        msg = 'It is full time of action with a score of ' + homeTeamScore + " for " + homeTeamName + " and " + awayTeamScore + " for " + awayTeamName + "."

        self.post(msg)

        fHS2 = open("output/awayTeamScore.txt", "w")
        fHS2.write("0")
        fHS2.close()

        fAS2 = open("output/awayTeamScore.txt", "w")
        fAS2.write("0")
        fAS2.close()

        fHN.close()
        fHS.close()
        fAN.close()
        fAS.close()

    def post(self, msg):
        page_id = 0
        facebook_access_token = 'put here'

        post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)
        payload = {
            'message': msg,
            'access_token': facebook_access_token
        }
        r = requests.post(post_url, data=payload)

        if r.status_code == 400:
            print("Error with Facebook Graph API, please check tokens.")
        else:
            print(r)
