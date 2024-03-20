Program został stworzony przy okazji pisania pracy licencjackiej.

Opis programu

Program umożliwia trenowanie agenta przy użyciu trzech różnych algorytmów:DQN, A2C oraz
PPO, w trzech grach: Cart Pole, Car Racing i Taxi. Przed rozpoczęciem każdej gry użytkownik musi
ustawić parametry dla tych algorytmów. Są to:

1. współczynnik uczenia α,
2. współczynnik dyskontowania γ,
3. wartość początkową ϵ,
4. liczbę gier do rozegrania.
   
Współczynnik uczenia (α) - określa, jak szybko agent ma się uczyć na podstawie nagród. Wyższa
wartość oznacza szybsze uczenie się.

Współczynnik dyskontowania przyszłych nagród (γ) - określa, jak bardzo agent będzie brał pod
uwagę przyszłe nagrody w porównaniu do bieżących nagród. Wartość bliższa 1 oznacza większe
uwzględnienie przyszłych nagród.

Ustawienie optymalnej ilości gier też jest ważnym parametrem. Większa liczba gier może prowadzić do lepszego uczenia, ale może również wymagać więcej czasu.

Wartość początkowa ϵ: Określa początkową wartość eksploracji agenta. Agent może działać w
sposób eksploracyjny (losowe działania) lub wykorzystywać swoją wiedzę (działanie na podstawie
najlepszych znanych akcji). Wartość ϵ wpływa na to, jak często agent będzie eksplorował w stosunku
do wykorzystywania swojej wiedzy.


Środowisko programu

Aplikacja została napisana w języku Python przy użyciu środowiska programistycznego PyCharm opracowanego przez firmę JetBrains. Wykorzystana wersja Pythona to 3.10.
Python posiada obszerną bibliotekę standardową oraz wiele bibliotek zewnętrznych, które wykorzystano w tej aplikacji. Są to Ray 2.5.0, który umożliwia implementację algorytmów, Gymnasium
0.26.3 służący do tworzenia środowisk gier, PyQt5 5.15.9 do tworzenia interfejsu użytkownika oraz
TensorFlow 2.12.0 do generowania wykresów.Wszystkie te biblioteki zostały zainstalowane w wirtualnym środowisku, aby zapewnić prawidłowe działanie aplikacji.



Program ma troche błędów i nie wszystko w nim działa. Umożliwił on jednak przeprowadzenie potrzebych testów i zebranie wyników. 
