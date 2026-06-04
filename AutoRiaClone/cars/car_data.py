from django.shortcuts import render

cars = [
    {
        "id": 1,
        "brand": "BMW",
        "model": "M5 Competition",
        "year": 2021,
        "price": 64999,
        "mileage": 45000,
        "engine": "4.4 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Київ",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/bmw.avif",
        "description": "Офіційний BMW M5 Competition у максимальній комплектації. Автомобіль повністю обслужений, без технічних зауважень. Повний M-пакет, проекція на лобове скло, камери 360°, адаптивна підвіска, вентиляція та підігрів сидінь. Готовий до будь-яких перевірок на СТО"
    },
    {
        "id": 2,
        "brand": "Audi",
        "model": "RS6",
        "year": 2022,
        "price": 84999,
        "mileage": 25000,
        "engine": "4.0 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Львів",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/audi.avif",
        "description": "Audi RS6 Avant з оригінальним підтвердженим пробігом. Потужний 4.0 TFSI, повний привід Quattro та спортивний вихлоп. Автомобіль у відмінному стані, без ДТП. Преміальна аудіосистема, панорама та максимальна комплектація."
    },
    {
        "id": 3,
        "brand": "Mercedes",
        "model": "E63 AMG",
        "year": 2020,
        "price": 72999,
        "mileage": 53000,
        "engine": "4.0 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Одеса",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/mers.avif",
        "description": "Mercedes-Benz E63 AMG у стані нового автомобіля. Регулярне обслуговування виключно на офіційному сервісі. AMG Performance пакет, панорамний дах, сидіння з пам'яттю та преміальна акустика Burmester."
    },

    {
        "id": 4,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2019,
        "price": 23999,
        "mileage": 90000,
        "engine": "2.5 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Харків",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/camri.avif",
        "description": "Надійний та комфортний седан для щоденного використання. Один власник в Україні, чесний пробіг. Автоматична коробка передач, двозонний клімат-контроль, камера заднього виду та безключовий доступ."
    },
    {
        "id": 5,
        "brand": "Volkswagen",
        "model": "Touareg",
        "year": 2021,
        "price": 45999,
        "mileage": 60000,
        "engine": "3.0 дизель",
        "transmission": "Автомат",
        "fuel": "Дизель",
        "region": "Київ",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/fol.avif",
        "description": "Volkswagen Touareg з потужним дизельним двигуном та повним приводом. Автомобіль повністю обслужений і не потребує вкладень. Шкіряний салон, пневмопідвіска, навігація та підігрів усіх сидінь. Відмінний варіант для далеких подорожей."
    },
    {
        "id": 6,
        "brand": "Tesla",
        "model": "Model S",
        "year": 2023,
        "price": 99999,
        "mileage": 12000,
        "engine": "Електро",
        "transmission": "Автомат",
        "fuel": "Електро",
        "region": "Львів",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/tesla.jpg",
        "description": "Tesla Model S Long Range у відмінному стані. Запас ходу понад 600 км на одному заряді. Автопілот, преміальний салон, панорамний дах та швидка зарядка. Сучасний електромобіль для комфортної та економної експлуатації."
    },
    {
        "id": 7,
        "brand": "Honda",
        "model": "Accord",
        "year": 2021,
        "price": 27999,
        "mileage": 65000,
        "engine": "1.5 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Дніпро",
        "image": "https://res.cloudinary.com/dcwkudf64/image/upload/v1780592268/honda_vnmajp.avif",
        "description": "Honda Accord у відмінному технічному стані. Надійний двигун, економна витрата пального та комфортний салон. Автомобіль повністю обслужений."
    },
    {
        "id": 8,
        "brand": "Ford",
        "model": "Mustang",
        "year": 2020,
        "price": 38999,
        "mileage": 42000,
        "engine": "5.0 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Київ",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/mustang.avif",
        "description": "Ford Mustang GT з атмосферним V8. Спортивний характер, відмінна динаміка та агресивний дизайн."
    },
    {
        "id": 9,
        "brand": "Skoda",
        "model": "Octavia",
        "year": 2022,
        "price": 24999,
        "mileage": 35000,
        "engine": "2.0 дизель",
        "transmission": "Автомат",
        "fuel": "Дизель",
        "region": "Вінниця",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/skoda.avif",
        "description": "Skoda Octavia з мінімальним пробігом. Просторий салон, сучасні системи безпеки та економний дизельний двигун."
    },
    {
        "id": 10,
        "brand": "Mazda",
        "model": "CX-5",
        "year": 2021,
        "price": 29999,
        "mileage": 58000,
        "engine": "2.5 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Львів",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/mazda.avif",
        "description": "Mazda CX-5 у максимальній комплектації. Шкіряний салон, адаптивний круїз-контроль та повний привід."
    },
    {
        "id": 11,
        "brand": "Porshe",
        "model": "911 Turbo S",
        "year": 2023,
        "price": 296999,
        "mileage": 71000,
        "engine": "5.0 бензин",
        "transmission": "Автомат",
        "fuel": "Бензин",
        "region": "Дніпро",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/photo-1614162692292-7ac56d7f7f1e.avif",
        "description": "САМАЛЬОТ"
    },
{
        "id": 12,
        "brand": "Lanos",
        "model": "Daewoo",
        "year": 2002,
        "price": 950,
        "mileage": 139000,
        "engine": "1.5 бензин",
        "transmission": "Механіка",
        "fuel": "Бензин",
        "region": "Львів",
        "image": "https://zijtttiunopqxzerspls.supabase.co/storage/v1/object/public/car-image/samalot.webp",
        "description": "САМАЛЬОТ"
    },

]


def home(request):
    filtered_cars = cars

    brand = request.GET.get("brand")
    year = request.GET.get("year")
    fuel = request.GET.get("fuel")
    transmission = request.GET.get("transmission")
    max_price = request.GET.get("max_price")

    if brand and brand != "all":
        filtered_cars = [c for c in filtered_cars if c["brand"] == brand]

    if year and year != "all":
        filtered_cars = [c for c in filtered_cars if str(c["year"]) == year]

    if fuel and fuel != "all":
        filtered_cars = [c for c in filtered_cars if c["fuel"] == fuel]

    if transmission and transmission != "all":
        filtered_cars = [c for c in filtered_cars if c["transmission"] == transmission]

    if max_price and max_price != "all":
        filtered_cars = [c for c in filtered_cars if c["price"] <= int(max_price)]

    context = {
        "cars": filtered_cars,
        "brands": sorted(list(set(c["brand"] for c in cars))),
    }

    return render(request, "cars/home.html", context)