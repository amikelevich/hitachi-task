import re
from playwright.sync_api import Page, expect

# --- Konfiguracja i dane testowe ---
BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
BACKPACK_NAME = "Sauce Labs Backpack"

# --- Funkcje pomocnicze ---
def perform_login(page: Page) -> None:
    """Wspólny krok logowania dla testów."""
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill(USERNAME)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()

# --- Scenariusze Testowe ---

def test_successful_login_and_redirect(page: Page):
    """
    Test 1: Sprawdź, czy użytkownik może się pomyślnie zalogować 
    i zostaje przekierowany na stronę z produktami.
    """
    perform_login(page)
    
    # Asercja 1: Sprawdzenie, czy URL to strona z produktami (inventory.html)
    expect(page).to_have_url(re.compile(r".*inventory\.html"))
    
    # Asercja 2: Sprawdzenie, czy nagłówek strony to "Products"
    expect(page.locator(".title")).to_have_text("Products")


def test_add_backpack_to_cart(page: Page):
    """
    Test 2: Zaloguj się, dodaj "Sauce Labs Backpack" do koszyka i sprawdź, 
    czy wskaźnik na ikonie koszyka zmienia się na "1", a przedmiot pojawia się w koszyku.
    """
    perform_login(page)
    
    # Dodanie przedmiotu do koszyka
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    # Asercja 1: Wskaźnik na ikonie koszyka wyświetla "1"
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    
    # Przejście do koszyka
    page.locator(".shopping_cart_link").click()
    
    # Asercja 2: Jesteśmy na stronie koszyka
    expect(page).to_have_url(re.compile(r".*cart\.html"))
    
    # Asercja 3: Produkt znajduje się na liście w koszyku
    expect(page.locator(".inventory_item_name")).to_have_text(BACKPACK_NAME)


def test_complete_checkout_flow(page: Page):
    """
    Test 3: Zaloguj się, dodaj przedmiot, przejdź do koszyka, kliknij checkout, 
    wypełnij formularz i zakończ zakup.
    """
    perform_login(page)
    
    # Dodanie dowolnego przedmiotu do koszyka i przejście do kasy
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator(".shopping_cart_link").click()
    page.locator('[data-test="checkout"]').click()
    
    # Asercja 1: Upewnienie się, że jesteśmy w pierwszym kroku płatności
    expect(page).to_have_url(re.compile(r".*checkout-step-one\.html"))
    
    # Wypełnienie formularza danych użytkownika
    page.locator('[data-test="firstName"]').fill("Jan")
    page.locator('[data-test="lastName"]').fill("Kowalski")
    page.locator('[data-test="postalCode"]').fill("00-001")
    page.locator('[data-test="continue"]').click()
    
    # Asercja 2: Przejście do kroku podsumowania zamówienia
    expect(page).to_have_url(re.compile(r".*checkout-step-two\.html"))
    
    # Zakończenie zakupu
    page.locator('[data-test="finish"]').click()
    
    # Asercja 3: Weryfikacja strony potwierdzenia i komunikatu o sukcesie
    expect(page).to_have_url(re.compile(r".*checkout-complete\.html"))
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")