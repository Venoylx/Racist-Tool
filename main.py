import requests
import socket
import webbrowser

# Replace 'YOUR_API_KEY' with your actual HaveIBeenPwned API key
HIBP_API_KEY = "YOUR_API_KEY"

def display_options():
    """Display a menu of options."""
    print("\nChoose an option:")
    print("1. Lookup an IP Address")
    print("2. Check if your email has been breached (HaveIBeenPwned)")
    print("3. Get your own IP address (after entering a username)")
    print("4. Delete a Discord Webhook")
    print("5. Rickroll yourself!")
    print("6. Exit")

def handle_choice(choice):
    """Handle the user's choice."""
    if choice == '1':
        ip_address = input("Enter the IP address to look up: ")
        lookup_ip(ip_address)
    elif choice == '2':
        email = input("Enter the email address to check: ")
        check_email_breach(email)
    elif choice == '3':
        username = input("Enter any username (this will give you your own IP): ")
        get_user_ip(username)
    elif choice == '4':
        webhook_url = input("Enter the Discord webhook URL to delete: ")
        delete_discord_webhook(webhook_url)
    elif choice == '5':
        open_rickroll()  # Option 5 triggers the Rickroll
    elif choice == '6':
        print("Exiting the program.")
        return False  # Signal to exit the loop
    else:
        print("Invalid choice. Please try again.")
    return True  # Continue the loop

def lookup_ip(ip_address):
    """Lookup information for the provided IP address."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Display the IP information
        print("\nIP Information:")
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data: {e}")

def check_email_breach(email):
    """Check if an email has been breached using the HaveIBeenPwned API."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        'hibp-api-key': HIBP_API_KEY,
        'User-Agent': 'python-script'
    }

    try:
        response = requests.get(url, headers=headers)
        
        # Check if the email is breached
        if response.status_code == 200:
            breaches = response.json()
            print(f"\nThe email '{email}' has been found in the following breaches:")
            for breach in breaches:
                print(f"- {breach['Name']}: Breached on {breach['BreachDate']}")
        elif response.status_code == 404:
            print(f"\nThe email '{email}' has not been found in any known breaches.")
        else:
            print(f"Error: Unable to check email. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def get_user_ip(username):
    """Get the user's own IP address."""
    try:
        # Get public IP address from an external service
        public_ip_response = requests.get("https://api.ipify.org?format=json")
        public_ip_response.raise_for_status()
        public_ip = public_ip_response.json()['ip']

        # Get local IP address
        local_ip = socket.gethostbyname(socket.gethostname())

        print(f"\nUsername: {username} (just for input)")
        print(f"Your Public IP Address: {public_ip}")
        print(f"Your Local IP Address: {local_ip}")
    except requests.exceptions.RequestException as e:
        print(f"Error getting public IP: {e}")
    except socket.error as e:
        print(f"Error getting local IP: {e}")

def delete_discord_webhook(webhook_url):
    """Delete a Discord webhook by sending a DELETE request to the webhook URL."""
    try:
        response = requests.delete(webhook_url)
        
        # Check the status of the deletion request
        if response.status_code == 204:
            print("\nWebhook deleted successfully!")
        elif response.status_code == 404:
            print("\nWebhook not found. Please check the URL.")
        else:
            print(f"Error: Unable to delete webhook. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting the webhook: {e}")

def open_rickroll():
    """Open Rick Astley's 'Never Gonna Give You Up' in the default web browser."""
    rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("You've been Rickrolled! Opening in your browser...")
    webbrowser.open(rickroll_url)

def main():
    while True:
        display_options()
        choice = input("Enter the number of your choice: ")
        if not handle_choice(choice):
            break  # Exit the loop if the user chooses to exit

if __name__ == "__main__":
    main()
