![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Warsztat &ndash; Przygotowanie projektu

Na początku musimy przygotować nasz projekt. W tym celu należy wykonać następujące kroki:
1. utworzyć repozytorium na **githubie** (nie zapomnij o dodaniu pliku `.gitignore`),
2. utworzyć środowisko wirtualne naszego projektu (pamiętaj, że pracujemy w Pythonie wersji 3.x),
3. zainstalować django i moduł do obsługi bazy danych - `psycopg2-binary`,
4. utworzyć projekt django,
5. utworzyć główną aplikację naszego projektu,
6. utworzyć bazę danych,
7. skonfigurować nasz projekt:
    * dodać konfigurację połączenia z bazą danych do pliku `settings.py`,
    * dodać wcześniej utworzoną aplikację do listy `INSTALLED_APPS` w pliku `settings.py`,
    * sprawdzić, czy inne ustawienia są poprawne (np. czy django będzie szukał szablonów w folderze aplikacji).
 

# Warsztat &ndash; Szablon bazowy

Przygotuj szablon bazowy **HTML**. Będzie to baza, na podstawie której, będziemy tworzyć kolejne podstrony.
Szablon powinien zawierać: 
1. tytuł strony,
2. menu zawierające przekierowania na następujące strony:
    * lista wszystkich sal (strona główna),
    * funkcjonalność dodawania nowej sali,
3. stopkę zawierającą informację na temat autora projektu.

# Warsztat &ndash; Model sali

Dodaj model reprezentujący salę. Powinien przechowywać takie informacje, jak:
* nazwa sali (pole tekstowe, maks 255 znaków, unikatowe),
* pojemność sali (pole typu liczbowego całkowitego),
* dostępność rzutnika (pole typu `boolean`).


# Warsztat &ndash; Widok dodawania sali

Utwórz widok, pozwalający na dodanie nowej sali. Umieść go pod adresem `/room/new/`.
Widok powinien:
* po wejściu metodą **GET** wyświetlić formularz zawierający następujące pola:
    * nazwa sali &ndash; tekst,
    * pojemność sali &ndash; liczba,
    * dostępność rzutnika &ndash; checkbox.
* po wejściu metodą **POST**:
    * sprawdzić, czy nazwa sali, nie jest pusta,
    * sprawdzić, czy sala o podanej nazwie, nie istnieje już w bazie danych,
    * sprawdzić, czy pojemność sali jest liczbą dodatnią;
    * jeśli dane są poprawne, zapisać nową salę do bazy i przekierować użytkownika na stronę główną,
    * jeśli są niepoprawne, powinien wyświetlić użytkownikowi odpowiedni komunikat.
    
Pamiętaj, żeby dodać odpowiedni wpis do pliku `urls.py`. 
Uzupełnij też odpowiedni link w szablonie bazowym.

> Nie przejmuj się tym, że nie ma jeszcze strony wyświetlającej wszystkie sale. Dodamy ją w następnym zadaniu.


# Warsztat &ndash; Lista wszystkich sal

Utwórz widok, na którym wyświetlisz listę wszystkich dostępnych sal.
Jeśli w bazie nie ma żadnej sali, powinien wyświetlić się komunikat:
**"Brak dostępnych sal"**.

Na tę chwilę dla każdej sali na liście, powinny wyświetlać się następujące informacje:
* nazwa sali &ndash; powinna być linkiem, przekierowującym na stronę ze szczegółowym widokiem sali (`/room/{id}/`),
* pojemność sali,
* dostępność sali (informacja, jeśli sala jest zajęta),
* dostępność rzutnika,
* przycisk edytuj &ndash; przekierowujący na stronę edycji sali (`/room/modify/{id}/`).
* przycisk usuń &ndash; przekierowujący na stronę usuwającą daną salę (`/room/delete/{id}`).
* przycisk zarezerwuj &ndash; przekierowujący do formularza rejestracji sali (`/room/reserve/{id}`).

Opisane wcześniej linki nie będą w tej chwili działały. Widoki do ich obsługi napiszemy w następnych zadaniach. 


# Warsztat &ndash; Usuwanie sali

Utwórz widok, usuwania sali. Niech widok obsługuje tylko metodę **GET**. Nie jest to najbezpieczniejsza opcja, 
ale na potrzeby naszego projektu w zupełności wystarczy. 

Widok powinien:
* być dostępny pod adresem `/room/delete/{id}`,
* na podstawie przekazanego w adresie parametru `id`, powinien wyszukać salę i ją usunąć
* na koniec, powinien przekierować użytkownika, do listy wszystkich dostępnych sal.


# Warsztat &ndash; Modyfikacja sali

Utwórz widok, pozwalający na zmodyfikowanie parametrów sali. 

Widok powinien:
* być dostępny pod adresem `/room/modify/{id}`,
* po wejściu metodą **GET** powinien wyszukać salę, na podstawie przekazanego w adresie parametru `id`
    a następnie wyświetlić formularz, pozwalający na edycję:
    * nazwy,
    * pojemności,
    * dostępności rzutnika,
* po wejściu metodą **POST**, powinien sprawdzić, czy:
    * pojemność jest większa od zera,
    * czy nazwa została wprowadzona,
    * czy nie istnieje w bazie sala o podanej nazwie,
    * jeśli dane są poprawne, powinien zapisać zmiany do bazy i przekierować użytkownika na listę wszystkich sal,
    * jeśli są niepoprawne, powinien poinformować o tym użytkownika.
    
> Podpowiedź:
> Możesz wzorować się na widoku dodawania nowej sali.


# Warsztat &ndash; Model rezerwacji

Utwórz model rezerwacji sali. Ma reprezentować rezerwację sali na dany dzień.
Powinien przechowywać następujące dany:
* datę,
* id sali,
* komentarz dodany przy rezerwacji.

Powinna być połączona z modelem sali relacją: jedna sala może mieć wiele całodniowych rezerwacji (każdą innego dnia).
Przy usuwaniu sali, powinny być usuwane jej rezerwacje.

> Podpowiedź: Aby sprawić, żeby dwa pola razem były unikalne, należy dodać do modelu meta klasę, ze zdefiniowaną
> krotką: `unique_togheter`.
> ##### Przykład:
> ```python
> class MyModel(models.Model):
>  field1 = models.CharField(max_length=50)
>  field2 = models.CharField(max_length=50)
>
>  class Meta:
>    unique_together = ('field1', 'field2',)
> ```


Nie zapomnij o migracji!


# Warsztat &ndash; Widok rezerwacji

Utwórz widok rezerwacji sali. Widok powinien:
* być dostępny pod adresem `/room/reserve/{id}`, gdzie `id`, to id sali,
* po wejściu metodą **GET** wyświetlić formularz zawierający następujące pola:
    * komentarz,
    * pole wyboru daty,
* po wejściu metodą **POST**:
    * zweryfikować, czy sala danego dnia nie jest już zarezerwowana,
    * sprawdzić, czy data nie jest z przeszłości,
    * zapisać rezerwację sali,
    * przekierować użytkownika do listy wszystkich sal.


# Warsztat &ndash; Szczegółowy widok sali

Dodaj widok, wyświetlający szczegółowe informacje, na temat sali.
Widok powinien: 
* wyświetlić wszystkie dane, na temat sali:
    * nazwę,
    * pojemność,
    * dostępność rzutnika,
* wyświetlić wszystkie przyszłe rezerwacje sali, wraz z komentarzami.

Ponadto powinna udostępnić linki do:
* strony edycji sali,
* strony usunięcia sali,
* strony rezerwacji sali.

Rezerwacje powinny być posortowane od najstarszej.

# Warsztat &ndash; Dostępność sali

Na liście wszystkich sal, dodaj kolumnę, w której wyświetlisz informację, czy sala jest zajęta.

> Podpowiedź: Będziesz musiał przekazać do szablonu aktualną datę.


# Warsztat &ndash; Aktualizacja widoku rezerwacji

Dodaj pod formularzem dodania nowej rezerwacji sali, dodaj listę wszystkich rezerwacji tej sali.

> Podpowiedź: Możesz bazować na szczegółowym widoku sali.


# Warsztat &ndash; Wyszukiwanie sali (dla chętnych)

Dodaj do strony głównej wyszukiwarkę. Umieść tam formularz przyjmujący wartości, 
według których program ma szukać wolnej sali:
* nazwę sali,
* minimalną potrzebną pojemność sali,
* obecność rzutnika.
Niech formularz wysyła dane metodą GET na adres /search.

Utwórz widok, w którym odbierzesz metodą GET dane z formularza wyszukiwania. 
Na podstawie tych danych zbuduj zapytanie do modeli, które wyszuka sale według podanych kryteriów.

Widok powinien zwrócić listę wolnych sal. Jeśli nie znajdzie żadnej, 
powinien pojawić się komunikat „Brak wolnych sal dla podanych kryteriów wyszukiwania”.

> Podpowiedź: Możesz wykorzystać szablon wyświetlający listę wszystkich sal.