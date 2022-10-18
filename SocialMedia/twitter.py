import tweepy

class Twitter:
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
        # Consumer keys and access tokens, used for OAuth
        CONSUMER_KEY = 'put here'
        CONSUMER_SECRET = 'put here'
        ACCESS_KEY = 'put here'
        ACCESS_SECRET = 'put here'

        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

        try:
            # Creation of the actual interface, using authentication
            api = tweepy.API(auth)

            # Sample method, used to update a status, you can write message whatever you want to post in twitter
            api.update_status(msg)
        except:
            print("Error with Twitter API, please check tokens.")