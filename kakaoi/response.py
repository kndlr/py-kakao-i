class SimpleText:
    def __init__(self, text : str):
        self.text = text

    def __str__(self):
        return self.text
        
    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<SimpleText {resolved}>"

    def __dict__(self):
        return {"simpleText":{"text": self.text}}

class SimpleImage:
    def __init__(self, image_url : str, alt_text : str):
        self.image_url = image_url
        self.alt_text = alt_text

    def __str__(self):
        return self.image_url
        
    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<SimpleImage {resolved}>"

    def __dict__(self):
        return {"simpleImage":{"imageUrl": self.image_url,"altText": self.alt_text}}

class Link:
    def __init__(self, *, pc : str = None, mobile : str = None, web : str = None):
        self.pc = pc
        self.mobile = mobile
        self.web = web

    def __str__(self):
        return self.web

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Link {resolved}>"

    def __dict__(self):
        self.dict = {}
        if self.pc: self.dict["pc"] = self.pc
        if self.mobile: self.dict["mobile"] = self.mobile
        if self.web: self.dict["web"] = self.web
        return self.dict

class Thumbnail:
    def __init__(self, *, image_url : str, link : Link = None, fixed_ratio : bool = False, width : int = False, height : int = False):
        self.image_url = image_url
        self.link = link
        self.fixed_ratio = fixed_ratio
        self.width = width
        self.height = height

    def __str__(self):
        return self.image_url

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Thumbnail {resolved}>"

    def __dict__(self):
        self.dict = {"imageUrl":self.image_url}
        if self.link: self.dict["link"] = self.link.__dict__()
        if self.fixed_ratio: self.dict["fixedRatio"] = self.fixed_ratio
        if self.fixed_ratio: self.dict["width"] = self.width
        if self.fixed_ratio: self.dict["height"] = self.height
        return self.dict
        
class Button:
    def __init__(self, *, label : str, action : str, link : str = None, message : str = None, phone : str = None, block_id : str = None, extra : dict = None):
        self.label = label
        self.action = action
        self.link = link
        self.message = message
        self.phone = phone
        self.block_id = block_id
        self.extra = extra

    def __str__(self):
        return self.label

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Button {resolved}>"

    def __dict__(self):
        self.dict = {"label":self.label,"action":self.action}
        if self.action == "link": self.dict["webLinkUrl"] = self.link
        if self.action in ["message","block"]: self.dict["messageText"] = self.message
        if self.action == "phone": self.dict["phoneNumber"] = self.phone
        if self.extra: self.dict["extra"] = self.extra
        return self.dict

class BasicCard:
    def __init__(self, *, title : str = None, description : str = None, thumbnail : Thumbnail, buttons : list = None):
        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.buttons = buttons

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
        return self.dict

class Profile:
    def __init__(self, *, nickname : str, image_url : str = None):
        self.nickname = nickname
        self.image_url = image_url

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<Profile {resolved}>"

    def __dict__(self):
        self.dict = {"nickname":self.nickname}
        if self.image_url: self.dict["imageUrl"] = self.image_url
        return self.dict

class CommerceCard:
    def __init__(self, *, description : str, price : int, discount : int = None, discount_rate : int = None, discounted_price : int = None, thumbnail : Thumbnail, profile : Profile = None, buttons : list):
        self.description = description
        self.price = price
        self.discount = discount
        self.discount_rate = discount_rate
        self.discounted_price = discounted_price
        self.thumbnail = thumbnail
        self.profile = profile
        self.buttons = buttons

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<CommerceCard {resolved}>"

    def __dict__(self):
        self.dict = {"commerceCard":{"description":self.description,"price":self.price,"currency":"won","thumbnails":[self.thumbnail.__dict__()],"buttons":[button.__dict__() for button in self.buttons]}}
        if self.discount: self.dict["commerceCard"]["discount"] = self.discount
        if self.discount_rate: self.dict["commerceCard"]["discountRate"] = self.discount_rate
        if self.discounted_price: self.dict["commerceCard"]["discountedPrice"] = self.discounted_price
        if self.profile: self.dict["commerceCard"]["profile"] = self.profile.__dict__()
        return self.dict

class ListItem:
    def __init__(self, *, title : str, description : str = None, image_url : str = None, link : Link = None):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.link = link

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

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<ListHeader {resolved}>"

    def __dict__(self):
        self.dict = {"title":self.title}
        if self.image_url: self.dict["imageUrl"] = self.image_url
        if self.link: self.dict["link"] = self.link.__dict__()
        return self.dict

class ListCard:
    def __init__(self, *, header : ListHeader, items : list, buttons : list = None):
        self.header = header
        self.items = items
        self.buttons = buttons

    def __repr__(self):
        resolved = " ".join(['%s=%r' % (attr[0], attr[1]) for attr in self.__dict__.items()])
        return f"<ListCard {resolved}>"

    def __dict__(self):
        self.dict = {"listCard":{"header":self.header.__dict__(),"items":[item.__dict__() for item in self.items]}}
        if self.buttons: self.dict["listCard"]["buttons"] = [button.__dict__() for button in self.buttons]
        return self.dict
