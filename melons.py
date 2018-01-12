"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders can inherit from."""

    def __init__(self, species, qty):
        """Initalize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas Melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    # it's good to make these as class attributes because they are common to the whole class 
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code

        super(InternationalMelonOrder, self).__init__(species, qty)

    def get_total(self):
        """Returns total for international melon orders less than 10."""

        # this is a classic example of polymorphism
        total_before_fee = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total_before_fee += 3

        return total_before_fee


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order that has no tax."""

    tax = 0.0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.passed_inspection = False

        super(GovernmentMelonOrder, self).__init__(species, qty)



    def mark_inspection(self, passed):
        """Updates passed_inspection based on boolean input."""
        
        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False