class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: int,
        clean_power: int,
        average_rating: int,
        count_of_ratings: int,
    ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_price = 0
        for car in cars:
            total_price += self.wash_single_car(car)
        return round(total_price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            clean_diffrence = self.clean_power - car.clean_mark
            wash_cost = (
                car.comfort_class
                * clean_diffrence
                * self.average_rating
                / self.distance_from_city_center
            )
            return round(wash_cost, 1)
        else:
            return 0.0

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            total_price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return round(total_price, 1)
        else:
            return 0.0

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rate)
            / self.count_of_ratings,
            1,
        )
