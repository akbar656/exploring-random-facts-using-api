import requests

#technology fact api

URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_technology_fact():
    try:
        response = requests.get(URL, timeout=5)

        #check if request was successful
        response.raise_for_status()
        fact_data = response.json()

        #print the fact nicely
        print("\n💡 Did you know?")
        print(fact_data.get("text", "No fact found"))

    except requests.exceptions.Timeout:
        print("⌚ Request timed out. please try again")
    except requests.exceptions.ConnectionError:
        print("🛜 No internet connection")
    except requests.exceptions.RequestException as e:
        print(f"🪧 Erro: {e}")



#main loop 
def main():
    print("💻 Random Technology Facts Generator")
    print("Type 'q' anytime to quit.\n ") 

    while True:
        user_input = input("press Enter to get a fact:")

        if user_input.lower() == 'q':
            print("👋Goodbye!")
            break
        get_random_technology_fact

if __name__ == "__main__":
    main()