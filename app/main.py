class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        return round((self.clean_power - car.clean_mark) * car.comfort_class * self.average_rating /
                     self.distance_from_city_center, 1)

    def wash_single_car(self, car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list):
        sum = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                sum += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return sum

    def rate_service(self, rating: int) -> None:
        rate_sum = (self.average_rating * self.count_of_ratings) + rating
        self.count_of_ratings += 1
        self.average_rating = round(rate_sum / self.count_of_ratings, 1)

