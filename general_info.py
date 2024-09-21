from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

url = "https://www.statsf1.com/en/"
pilot = "guanyu zhou"
pilot = pilot.replace(" ", "-")

driver_url = url + pilot +".aspx" 

driver = webdriver.Firefox()
driver.set_window_size(600,600)

driver.get(driver_url)
sleep(3.5)

def general_info():
    chmp = []
    full_name = driver.find_element(By.TAG_NAME,"strong").text
    nation = driver.find_element(By.ID, "ctl00_CPH_Main_HL_Pays").text
    first_race = driver.find_element(By.ID,"ctl00_CPH_Main_HL_FirstGP").text
    last_race = driver.find_element(By.ID,"ctl00_CPH_Main_HL_LastGP").text
    total_grand_prix = driver.find_element(By.ID, "ctl00_CPH_Main_HL_StatsGP").text
    print(f"Full Name:{full_name}")
    print(f"Nation:{nation}")
    print(f"First Race: {first_race}")
    print(f"Last Race:{last_race}")
    print(f"Races Entered:{total_grand_prix}")

    try:
        races_won1 = driver.find_element(By.ID,"ctl00_CPH_Main_HL_StatsVictoire").text 
        print(f"Wins:{races_won1}")
    except NoSuchElementException:
        pass

    try:
        pole_count = driver.find_element(By.ID,"ctl00_CPH_Main_HL_StatsPole").text 
        print(f"Poles:{pole_count}")
    except NoSuchElementException:
        pass

    try:
        fl = driver.find_element(By.ID,"ctl00_CPH_Main_HL_StatsMeilleurTour").text 
        print(f"Fastest laps:{fl}")
    except NoSuchElementException:
        pass

    try:
        podium = driver.find_element(By.ID,"ctl00_CPH_Main_HL_StatsPodium").text 
        print(f"Podiums:{podium}")
    except NoSuchElementException:
        pass
    
    try:
        hat_trick = driver.find_element(By.ID,"ctl00_CPH_Main_HL_StatsHatT").text 
        print(f"Hat Tricks:{hat_trick}")
    except NoSuchElementException:
        pass

    try:
        g_slam = driver.find_element(By.ID,"ctl00_CPH_Main_HL_StatsChelem").text 
        print(f"Grand Slams:{g_slam}")
    except NoSuchElementException:
        pass

    try:
        total_points = driver.find_element(By.ID,"ctl00_CPH_Main_HP_StatsPoint").text 
        total_points = total_points.replace(" ","")
        print(f"Total Points:{total_points}")
    except NoSuchElementException:
        pass

    xpth = """//*[@id="content"]/div[4]/strong"""
    is_champ = driver.find_element(By.XPATH, xpth)

    if "Champion" in is_champ.text and len(is_champ.text)==8:
        best_result = driver.find_element(By.CLASS_NAME,"pilotechp")
        best_result_parent = best_result.find_elements(By.TAG_NAME,"a")
        delete = driver.find_element(By.ID,"bar-Container")
        delete_sub = delete.find_elements(By.TAG_NAME,"a")
        a = 0
        print("Champion years:",end=",")
        for i in best_result_parent:
            if i in delete_sub:
                pass
            else:
                print(i.text)
                a += 1
        print(f"Championships won:{a}")
    else:
        xpth = """//*[@id="content"]/div[4]/strong"""
        best_result1 = driver.find_element(By.XPATH,xpth).text
        print(best_result1)

    driver.quit()
general_info()