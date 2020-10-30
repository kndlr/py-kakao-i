from .model import *

class SimpleText(Forwardable):
    def __init__(self, text : str, **kwargs):
        self.text = text
        super().__init__(**kwargs)

    def __str__(self):
        return self.text
        
    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<SimpleText {resolved}>"

    def __dict__(self):
        self.dict = {"simpleText":{"text": self.text}}
        super().__dict__()
        return self.dict

class SimpleImage(Forwardable):
    def __init__(self, image_url : str, alt_text : str, **kwargs):
        self.image_url = image_url
        self.alt_text = alt_text
        super().__init__(**kwargs)

    def __str__(self):
        return self.image_url
        
    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<SimpleImage {resolved}>"

    def __dict__(self):
        self.dict = {"simpleImage":{"imageUrl": self.image_url,"altText": self.alt_text}}
        super().__dict__()
        return self.dict

class BasicCard(Forwardable):
    def __init__(self, *, title : str = None, description : str = None, thumbnail : Thumbnail, buttons : list = None, **kwargs):
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.buttons = buttons
        super().__init__(**kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<BasicCard {resolved}>"

    def __dict__(self):
        self.dict = {"basicCard":{"thumbnail":self.thumbnail.__dict__()}}
        if self.title: self.dict["basicCard"]["title"] = self.title
        if self.description: self.dict["basicCard"]["description"] = self.description
        if self.buttons: self.dict["basicCard"]["buttons"] = [button.__dict__() for button in self.buttons]
        super().__dict__()
        return self.dict

class CommerceCard(Forwardable):
    def __init__(self, *, description : str, price : int, discount : int = None, discount_rate : int = None, discounted_price : int = None, thumbnail : Thumbnail, profile : Profile = None, buttons : list, **kwargs):
        self.description = description
        self.price = price
        self.discount = discount
        self.discount_rate = discount_rate
        self.discounted_price = discounted_price
        self.thumbnail = thumbnail
        self.profile = profile
        self.buttons = buttons
        super().__init__(**kwargs)

    def __str__(self):
        return self.description

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<CommerceCard {resolved}>"

    def __dict__(self):
        self.dict = {"commerceCard":{"description":self.description,"price":self.price,"currency":"won","thumbnails":[self.thumbnail.__dict__()],"buttons":[button.__dict__() for button in self.buttons]}}
        if self.discount: self.dict["commerceCard"]["discount"] = self.discount
        if self.discount_rate: self.dict["commerceCard"]["discountRate"] = self.discount_rate
        if self.discounted_price: self.dict["commerceCard"]["discountedPrice"] = self.discounted_price
        if self.profile: self.dict["commerceCard"]["profile"] = self.profile.__dict__()
        super().__dict__()
        return self.dict

class ListItem:
    def __init__(self, *, title : str, description : str = None, image_url : str = None, link : Link = None):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link

    def __str__(self):
        return self.title

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<ListItem {resolved}>"

    def __dict__(self):
        self.dict = {"title":self.title}
        if self.description: self.dict["description"] = self.description
        if self.image_url: self.dict["imageUrl"] = self.image_url
        if self.link: self.dict["link"] = self.link.__dict__()
        return self.dict

class ListHeader:
    def __init__(self, *, title : str, image_url : str = None, link : Link = None):
        self.title = title
        self.image_url = image_url
        self.link = link

    def __str__(self):
        return self.title

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<ListHeader {resolved}>"

    def __dict__(self):
        self.dict = {"title":self.title}
        if self.image_url: self.dict["imageUrl"] = self.image_url
        if self.link: self.dict["link"] = self.link.__dict__()
        return self.dict

class ListCard(Forwardable):
    def __init__(self, *, header : ListHeader, items : list, buttons : list = None, **kwargs):
        self.header = header
        self.items = items
        self.buttons = buttons
        super().__init__(**kwargs)

    def __str__(self):
        return self.header.title

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<ListCard {resolved}>"

    def __dict__(self):
        self.dict = {"listCard":{"header":self.header.__dict__(),"items":[item.__dict__() for item in self.items]}}
        if self.buttons: self.dict["listCard"]["buttons"] = [button.__dict__() for button in self.buttons]
        super().__dict__()
        return self.dict

class CarouselHeader:
    def __init__(self, *, title : str, description : str, thumbnail : Thumbnail):
        self.title = title
        self.description = description
        self.thumbnail = thumbnail

    def __str__(self):
        return self.title

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<CarouselHeader {resolved}>"

    def __dict__(self):
        self.dict = {"title":self.title,"description":self.description,"thumbnail":self.thumbnail.__dict__()}
        return self.dict

class Carousel:
    def __init__(self, *, items : list, header : CarouselHeader = None):
        if all([list(item.__dict__().keys())[0] for item in items]):
            self.type = list(items[0].__dict__().keys())[0]
        self.items = items
        self.header = header

    def __str__(self):
        return self.type

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<CarouselHeader {resolved}>"

    def __dict__(self):
        self.dict = {"carousel":{"type":self.type,"items":[item.__dict__() for item in self.items]}}
        if self.header: self.dict["carousel"]["header"] = self.header.__dict__()
        return self.dict
