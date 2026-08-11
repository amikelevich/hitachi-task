# Zadanie Rekrutacyjne

## 1. Krótki opis

Celem zadania było stworzenie zautomatyzowanych testów dla aplikacji SauceDemo, wykorzystując Python, pytest oraz Playwright, przy wsparciu modelu **Gemini Pro**.

Zastosowałam ustrukturyzowany prompt, nadając modelowi rolę Senior QA Automation Engineera. Dzięki temu wygenerowany kod od razu opierał się na dobrych praktykach. Zdefiniowałam również wymagany stos technologiczny, ścieżki biznesowe (logowanie, obsługa koszyka, proces checkoutu) oraz wymogi techniczne.

Model poprawnie zinterpretował polecenie i wygenerował czysty i czytelny skrypt. Po wygenerowaniu kodu sprawdziłam, czy testy są od siebie całkowicie odizolowane. Stan aplikacji jest odpowiednio resetowany przed każdym scenariuszem za pomocą funkcji `perform_login()`. Upewniłam się również, że każdy kluczowy krok kończy się asercją (obiekt `expect`). Gwarantuje to, że testy faktycznie walidują zachowanie aplikacji. Po analizie uruchomiłam skrypty lokalnie.

Praca nad tym zadaniem pokazała mi, że wykorzystanie AI jako asystenta programowania znacząco przyspiesza tworzenie kodu. Niemniej jednak, rola inżyniera QA pozostaje kluczowa przy projektowaniu scenariuszy, dostarczaniu odpowiedniego kontekstu oraz końcowej weryfikacji, czy wygenerowany kod faktycznie testuje zamierzoną logikę.

---

## 2. Użyty Prompt AI

```
Jesteś Senior QA Automation Engineer. Twoim zadaniem jest napisanie trzech zautomatyzowanych testów dla aplikacji webowej https://www.saucedemo.com/.

Stos technologiczny:
- Język - Python
- Framework testowy - pytest
- Narzędzie - Playwright

Scenariusze testowe:
Napisz testy dla poniższych 3 ścieżek użytkownika. Użyj danych logowania dostępnych na stronie głównej (użytkownik: standard_user, hasło: secret_sauce).

1. Sprawdź, czy użytkownik może się pomyślnie zalogować i zostaje przekierowany na stronę z produktami.
2. Zaloguj się, dodaj "Sauce Labs Backpack" do koszyka i sprawdź, czy wskaźnik na ikonie koszyka zmienia się na "1", a przedmiot pojawia się na stronie koszyka.
3. Zaloguj się, dodaj dowolny przedmiot do koszyka, przejdź do koszyka, kliknij "checkout", wypełnij formularz danych użytkownika (Imię, Nazwisko, Kod pocztowy), przejdź dalej i zakończ zakup. Zweryfikuj, czy pojawia się komunikat o złożeniu zamówienia.

Wymagania dotyczące kodu:
1. Kod musi być czysty, czytelny i zgodny z dobrymi praktykami.
2. Umieść jasne asercje dla każdego kluczowego kroku, aby test faktycznie weryfikował zachowanie aplikacji.
3. Upewnij się, że testy są od siebie całkowicie niezależne.

Elementy do dostarczenia:
1. Kompletny skrypt testowy w języku Python.
2. Zawartość pliku requirements.txt niezbędnego do uruchomienia środowiska.
3. Krótka instrukcja krok po kroku, jak zainstalować zależności i uruchomić testy w terminalu.
```

---

## 3. Jak uruchomić testy

**Wymagania wstępne:** Zainstalowany język Python 3.

1. **Klonowanie repozytorium:**

   ```bash
   git clone https://github.com/amikelevich/hitachi-task.git
   ```

2. **Utworzenie i aktywacja wirtualnego środowiska w folderze z projektem:**

   ```
   python -m venv venv

   # Aktywacja na systemie Windows:
   venv\Scripts\activate

   # Aktywacja na systemie macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalacja wymaganych pakietów:**

   ```
   pip install -r requirements.txt
   ```

4. **Instalacja przeglądarki dla narzędzia Playwright:**

   ```
   playwright install
   ```

5. **Uruchomienie testów:**

   ```
   pytest test_saucedemo.py
   ```

   Aby uruchomić testy w trybie widocznym:

   ```
   pytest test_saucedemo.py --headed
   ```
