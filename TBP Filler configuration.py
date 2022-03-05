from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
startTime = time.time()
service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.get("https://interactivity-prod-viacom18.web.app/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").click()
driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("aniket.gupta@rws.com")
driver.find_element(By.XPATH, "//*[@id='password']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Viacom@123")
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/main/div/form/button/span[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[3]/div[2]").click()


# Click on Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[1]/div/div/ul/div[2]/div[2]").click()

# Click on Create Quiz
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div/div[2]/div[1]/p").click()
time.sleep(3)

# Select Channel
driver.find_element(By.CSS_SELECTOR, "input[value=Colors]").click()

time.sleep(1)

# Click on show list
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[1]/div/div").click()
time.sleep(3)

# Click on the show
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[15]").click()

#input("Check for the correct show selected: ")

time.sleep(2)

# Save and Next
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div/div/div[3]/button").click()

time.sleep(2)

# Click on the menu
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/div").click()

# Click on the Create Line Up
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[1]/div/div/ul/li[6]").click()

# Click on add new episode icon
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div[2]/label").click()

# Insert the episode name
driver.find_element(By.XPATH, "//*[@id='lineup']").send_keys("EP 26 Final ")


# Click on add button to save the new created episode
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div/div[2]/label[1]").click()
time.sleep(1)

input("Check whether the created eipsode is reflecting or not and make sure that you come back to create line up page if wish to continue: ", )


# Click on the Episode section
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div/div").click()

# Select the episode
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]").click()
# Haere above li[2] means second in the list, li[1] is for select and it goes on to li[3], li[4] so on. The latest will always be li[2].


# Click on the upload the questions button and upload
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[2]/div[2]/span[1]/label/span[1]/input").send_keys("C:\\Users\\aniket.gupta\\Downloads\\EP26.xlsx")
time.sleep(3)

# Click on Save The Questions
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[2]/div[2]/span[2]/label").click()

# Click on Go To Filler
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[2]/div[2]/span[3]/label").click()

def addfiller(FN,FT,CDN):

    # Click on Add Filler
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div/div/span[1]/label").click()

    # Click on Filler media type
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div").click()
    time.sleep(2)

    # Selecting the filler media as Image
    driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[1]").click()

    # Selecting Potrait Option Type
    driver.find_element(By.CSS_SELECTOR, "input[value=Portrait]").click()

    # Selecting non-sponsered
    driver.find_element(By.CSS_SELECTOR, "input[value=non-sponsored]").click()

    # Entering the filler name
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[1]/div/input").send_keys(FN)

    # Entering the CDN URL
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/span/div/div/input").send_keys(CDN)

    # Entering Filler Text
    driver.find_element(By.XPATH, "//*[@id='standard-basic']").send_keys(FT)

    # Save
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[5]/span[1]/label").click()

def adddfpfiller(FN,FT,VU,ATU):

    # Click on Add Filler
    driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div/div/span[1]/label").click()

    # Click on Filler media type
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div").click()
    time.sleep(1)

    # Selecting the filler media as Image
    driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[5]").click()

    # Select Ad type as Video
    driver.find_element(By.CSS_SELECTOR, "input[value=videoad]").click()

    # Enter the Video Source
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[3]/div/div[1]/div/input").send_keys(VU)

    # Enter the Ad Tag URL
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[3]/div/div[2]/div/input").send_keys(ATU)

    # Entering the filler name
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[1]/div/input").send_keys(FN)

    # Entering Filler Text
    driver.find_element(By.XPATH, "//*[@id='standard-basic']").send_keys(FT)

    # Save
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[5]/span[1]/label").click()

# Common Filler Urls

Welcome	=	"https://v3img.voot.com/tbp/fillers/VA/WelcomeToTBP_Video_Along.png"
Tasveer_Se_Taqdeer_Tak_	=	"https://v3img.voot.com/tbp/fillers/VA/TasveerSeTaqdeerTak_Video_Along.png"
How_To_Play	=	"https://v3img.voot.com/tbp/fillers/VA/HowToPlay_Video_Along.png"
India_Wale_Life_Line	=	"https://v3img.voot.com/tbp/fillers/VA/IndiaWaleLifeline_VideoALong.png"
Are_you_ready_Hindi	=	"https://v3img.voot.com/tbp/fillers/VA/04_RanveerIsReady_Hindi_Video_Along.png"
Are_you_ready_English	=	"https://v3img.voot.com/tbp/fillers/VA/04_RanveerIsReady_English_Video_Along.png"
Game_Time	=	"https://v3img.voot.com/tbp/fillers/VA/LetsPlay_Video_Along.png"
Ghar_Baithe_Jeeto	=	"https://v3img.voot.com/tbp/fillers/VA/GharBaitheJeeto.png"
Dream_Hindi	=	"https://v3img.voot.com/tbp/fillers/VA/09_Dream_Hindi_Video_Along.png"
Dream_English	=	"https://v3img.voot.com/tbp/fillers/VA/09_DreamEnglish_Video_Along.png"
Game_Starts_Soon_English	=	"https://v3img.voot.com/tbp/fillers/VA/06_StayTuned_English_Video_Along.png"
Game_Starts_Soon_Hindi	=	"https://v3img.voot.com/tbp/fillers/VA/06_StayTuned_Hindi_Video_Along.png"
Will_Be_Back	=	"https://v3img.voot.com/tbp/fillers/VA/WillBeBack_Video_along.png"
Stay_Tuned_English	=	"https://v3img.voot.com/tbp/fillers/VA/16_NextQuestionEnglish_Video_Along.png"
Stay_Tuned_Hindi	=	"https://v3img.voot.com/tbp/fillers/VA/16_NextQuestion_Hindi.png"
Congratulations = f"{input('Paste the Congratulations URL correctly ', )}"
Welcome_Contestant_Kajol = f"{input('Paste the Welcome Kajol URL correctly ', )}"
Welcome_Contestant_Karan = f"{input('Paste the Welcome Karan URL correctly ', )}"

# Video Ad Credentials
#video_source = "https://v3img.voot.com/tbp/VOOT_Bumper_Final.mp4"
#ad_tag_url = "https://pubads.g.doubleclick.net/gampad/ads?iu=/21633895671/PlayAlong/PlayAlongVideo&description_url=[placeholder]&tfcd=0&npa=0&sz=640x360%7C640x480%7C850x478&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator="

# Extra Fillers

#extra = f"{input('Paste the exra filler URL: ', )}"

# Only Image URLs

I1	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q01.png"
I2	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q02.png"
I3	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q03.png"
I4	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q04.png"
I5	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q05.png"
I6	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q06.png"
I7	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q07.png"
I8	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q08.png"
I9	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q09.png"
I10	=	"https://v3img.voot.com/tbp/EP26/10_PreQuizImage_Q10.png"

# Image with question URLs

Q1	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q01.png"
Q2	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q02.png"
Q3	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q03.png"
Q4	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q04.png"
Q5	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q05.png"
Q6	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q06.png"
Q7	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q07.png"
Q8	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q08.png"
Q9	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q09.png"
Q10	=	"https://v3img.voot.com/tbp/EP26/11_PreQuizImagewithQuestion_Q10.png"

# Answer Filler Urls

A1	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q01.png"
A2	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q02.png"
A3	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q03.png"
A4	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q04.png"
A5	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q05.png"
A6	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q06.png"
A7	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q07.png"
A8	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q08.png"
A9	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q09.png"
A10	=	"https://v3img.voot.com/tbp/EP26/15_PostQuesTrivia_Q10.png"

# Adding Fillers related to questions

addfiller("Image 1", "Image 1", I1)
addfiller("Image 2", "Image 2", I2)
addfiller("Image 3", "Image 3", I3)
addfiller("Image 4", "Image 4", I4)
addfiller("Image 5", "Image 5", I5)
addfiller("Image 6", "Image 6", I6)
addfiller("Image 7", "Image 7", I7)
addfiller("Image 8", "Image 8", I8)
addfiller("Image 9", "Image 9", I9)
addfiller("Image 10", "Image 10", I10)



addfiller("Question 1", "Question 1", Q1)
addfiller("Question 2", "Question 2", Q2)
addfiller("Question 3", "Question 3", Q3)
addfiller("Question 4", "Question 4", Q4)
addfiller("Question 5", "Question 5", Q5)
addfiller("Question 6", "Question 6", Q6)
addfiller("Question 7", "Question 7", Q7)
addfiller("Question 8", "Question 8", Q8)
addfiller("Question 9", "Question 9", Q9)
addfiller("Question 10", "Question 10", Q10)


addfiller("Answer 1", "Answer 1", A1)
addfiller("Answer 2", "Answer 2", A2)
addfiller("Answer 3", "Answer 3", A3)
addfiller("Answer 4", "Answer 4", A4)
addfiller("Answer 5", "Answer 5", A5)
addfiller("Answer 6", "Answer 6", A6)
addfiller("Answer 7", "Answer 7", A7)
addfiller("Answer 8", "Answer 8", A8)
addfiller("Answer 9", "Answer 9", A9)
addfiller("Answer 10", "Answer 10", A10)


# Adding Common Fillers
addfiller("Welcome","Welcome",Welcome)
addfiller("Tasveer Se Taqdeer Tak ","Tasveer Se Taqdeer Tak ",Tasveer_Se_Taqdeer_Tak_)
addfiller("How To Play","How To Play",How_To_Play)
#addfiller("India Wale Life Line","India Wale Life Line",India_Wale_Life_Line)
#addfiller("Are you ready Hindi","Are you ready Hindi",Are_you_ready_Hindi)
#addfiller("Are you ready English","Are you ready English",Are_you_ready_English)
addfiller("Game Time","Game Time",Game_Time)
addfiller("Ghar Baithe Jeeto","Ghar Baithe Jeeto",Ghar_Baithe_Jeeto)
addfiller("Dream Hindi","Dream Hindi",Dream_Hindi)
addfiller("Dream English","Dream English",Dream_English)
addfiller("Game Starts Soon English","Game Starts Soon English",Game_Starts_Soon_English)
addfiller("Game Starts Soon Hindi","Game Starts Soon Hindi",Game_Starts_Soon_Hindi)
addfiller("Will Be Back","Will Be Back",Will_Be_Back)
addfiller("Stay Tuned English","Stay Tuned English",Stay_Tuned_English)
addfiller("Stay Tuned Hindi","Stay Tuned Hindi",Stay_Tuned_Hindi)

# Extra Filler
#addfiller("Happy New Year", "Happy New Year", extra)

# Adding Congratulations filler
addfiller("Congratulation", "Congratulation", Congratulations)

# Adding Welcome Contestant filler
addfiller("Contestant Kajol ", "Contestant Kajol", Welcome_Contestant_Kajol)
addfiller("Contestant Karan ", "Contestant Karan", Welcome_Contestant_Karan)

# Adding Stay Tuned English filler 7 more times with proper nomenclature
for i in range(2,9):
    addfiller("Stay Tuned English " + str(i),"Stay Tuned English " + str(i),Stay_Tuned_English)

# Adding Stay Tuned Hindi filler 7 more times with proper nomenclature
for i in range(2,9):
    addfiller("Stay Tuned Hindi " + str(i),"Stay Tuned Hindi " + str(i),Stay_Tuned_Hindi)

# Adding Will be back filler 5 more times with proper nomenclature
for i in range(2,6):
    addfiller("Will Be Back " + str(i),"Will Be Back " + str(i),Will_Be_Back)

# Adding India Wale filler 2 more times with proper nomenclature
#for i in range(2,3):
    #addfiller("India Wale Lifline " + str(i),"India Wale Lifeline " + str(i),India_Wale_Life_Line)

# Adding Tasveer Se Taqdeer Tak filler 2 more times with proper nomenclature
for i in range(2,4):
    addfiller("Tasveer Se Taqdeer Tak " + str(i), "Tasveer Se Taqdeer Tak " + str(i), Tasveer_Se_Taqdeer_Tak_)

# Adding Ghar Baithe Jeeto filler 2 more times with proper nomenclature
for i in range(2,3):
    addfiller("Ghar Baithe Jeeto " + str(i),"Ghar Baithe Jeeto " + str(i), Ghar_Baithe_Jeeto)

# Adding Dream filler 2 more times with proper nomenclature
for i in range(2,4):
    addfiller("Dream English " + str(i),"Dream English " + str(i), Dream_English)

# adding dfp filler
#for i in range(2,9):
    #adddfpfiller("Video Ad " + str(i), "Video Ad " + str(i), video_source, ad_tag_url)

# Click on save and next for the filler
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div/div/span[2]/label").click()

# Click on episode selection
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[1]/div/div/div/div").click()

# Click on episode
driver.find_element(By.XPATH, "//*[@id='menu-']/div[3]/ul/li[2]").click()

# Click on the menu
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[1]/div/div/div").click()

# Click on Glossary
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[1]/div/div/ul/li[9]").click()
time.sleep(1)

# Clearning and entering Playing for glossary
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[7]/div/input").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[7]/div/input").send_keys("The right answer gets you [[score]] points.")

# Click on Save
driver.find_element(By.XPATH, "//*[@id='call-for-entry']/div[2]/div/div/div[2]/div[10]/div/span/label").click()

print ('The script took {0} second !'.format(time.time() - startTime))