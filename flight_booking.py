from abc import ABC, abstractmethod
import datetime



class Logger:
    @staticmethod
    def log(message):
        print(f"[LOG - {datetime.datetime.now().strftime('%H:%M:%S')}]: {message}")




class Flight:
    def __init__(self, flight_no, origin, destination, departure_time, arrival_time, capacity=150):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.capacity = capacity

    def reserve_seat(self):
        if self.capacity > 0:
            self.capacity -= 1
            return True
        return False

    def cancel_seat(self):
        self.capacity += 1



class Passenger:
    def __init__(self, name, email):
        self.name = name
        self.email = email




class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        if amount <= 0:
            Logger.log("Geçersiz ödeme tutarı.")
            return False
        print(f"[KREDI KARTI] {self.card_number} nolu karttan {amount} TL tahsil edildi.")
        return True


class WireTransferPayment(Payment):
    def __init__(self, iban):
        self.iban = iban

    def pay(self, amount):
        if amount <= 0:
            Logger.log("Geçersiz ödeme tutarı.")
            return False
        print(f"[HAVALE] {self.iban} IBAN numarasına {amount} TL transfer onaylandı.")
        return True


class CashPayment(Payment):
    def pay(self, amount):
        if amount <= 0:
            Logger.log("Geçersiz ödeme tutarı.")
            return False
        print(f"[NAKIT] {amount} TL nakit ödeme alındı.")
        return True




class Notification(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass


class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"[E-POSTA GÖNDERİLDİ] Alıcı: {recipient} -> Mesaj: {message}")


class SMSNotification(Notification):
    def send(self, recipient, message):
        print(f"[SMS GÖNDERİLDİ] Alıcı: {recipient} -> Mesaj: {message}")



class Booking:
    def __init__(self, booking_id, flight, passenger, payment: Payment, notification: Notification):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.payment = payment
        self.notification = notification
        self.status = "Beklemede"

    def confirm(self, amount):
        if not self.flight.reserve_seat():
            Logger.log(f"(Booking {self.booking_id}) -> Kapasite dolu, rezervasyon yapılamadı.")
            self.status = "Başarısız"
            return

        if self.payment.pay(amount):
            self.status = "Onaylandı"
            Logger.log(f"(Booking {self.booking_id}) -> Rezervasyon {self.booking_id} onaylandı.")
            self.notification.send(self.passenger.email,
                                   f"Sayın {self.passenger.name}, {self.flight.flight_no} uçuşunuz onaylanmıştır.\nRezervasyon ID: {self.booking_id} | Durum: {self.status}")
        else:
            Logger.log(f"(Booking {self.booking_id}) -> Ödeme başarısız, rezervasyon onaylanmadı.")
            self.flight.cancel_seat()
            self.status = "Başarısız"

    def cancel(self):
        if self.status == "Onaylandı":
            self.flight.cancel_seat()
            self.status = "İptal Edildi"
            Logger.log(f"(Booking {self.booking_id}) -> Rezervasyon {self.booking_id} iptal edildi.")
            self.notification.send(self.passenger.email,
                                   f"Uçuşunuz iptal edilmiştir.\nRezervasyon ID: {self.booking_id} | Durum: {self.status}")
        else:
            Logger.log(f"(Booking {self.booking_id}) -> İptal edilemedi, rezervasyon onaylı değil.")



class FlightSearch:
    def __init__(self, flights):
        self.flights = flights

    def search(self, origin, destination, date):
        results = [f for f in self.flights if f.origin == origin and f.destination == destination and f.departure_time.startswith(date)]
        return results



if __name__ == "__main__":
    flight = Flight("TK1923", "IST", "JFK", "2026-04-12 10:00", "2026-04-12 15:00")
    passenger = Passenger("Ahmet Yılmaz", "ahmet@email.com")

    search_engine = FlightSearch([flight])
    found = search_engine.search("IST", "JFK", "2026-04-12")
    print("Arama Sonucu:", [f.flight_no for f in found])

    booking1 = Booking("B-001", flight, passenger, CreditCardPayment("1234-5678-9012-3456"), EmailNotification())
    booking1.confirm(1500.0)

    booking2 = Booking("B-002", flight, passenger, WireTransferPayment("TR12 3456 7890 1234 5678 9012 34"), EmailNotification())
    booking2.confirm(1500.0)

    booking3 = Booking("B-003", flight, passenger, CashPayment(), EmailNotification())
    booking3.confirm(1500.0)
    booking3.cancel()
