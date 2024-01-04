from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen ,SlideTransition
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.uix.textinput import TextInput
from kivy.graphics import Ellipse, Color, Line, Rectangle
from kivy.graphics.texture import Texture
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
#from kivy.garden.zbarcam import ZBarCam
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.core.window import Window
from math import sin
import time
from io import BytesIO
import firebase_admin
from firebase_admin import credentials,db,storage
##from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
cred=credentials.Certificate({
  "type": "service_account",
  "project_id": "tryhackathon",
  "private_key_id": "6b5100d7909676ddb2d16033abe01d0d7e7d6077",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCila3K9vRBRkEe\nVdGD8Z7fEM6K5ADWyLg4R40QuKGTgKS5ETyZOz1CfyaC/djz0t9e5HxihOm7Ve0y\nFRWMNxmPC/e6xsF9FYX1y/3DA9BleOJp0htCTo1iDurds4iCPBxD3P6BDnh78zuK\n7PEdvlkDKn9nlLyj/UKniUIrP8fU7ZtdinmXrLqhXL0M/zAiRyEcZKsPPrIsourG\nca/t41oY/Bk60yTaNZHVBzvK0dy6xYfmEtq5+GslXzpS/CAD/+aXFPkC8rXLiTJY\nUQtUNvWFL1LnJsuHkQNJVpo86qVkqpQk4a2wbFdnqXKKXqmTectlklqlwsVeYMl5\npt34qcotAgMBAAECgf8iPePxxeaA2OBeGIpH1QY2H2lgrHnWF/AJ6l02EwH0pDi3\nwX7scXg1c7y+BI3szDy/KjVdinYE6SlLovp8IslUl0YAJbFv5q3lVqaGAVz4AhMC\ntn2HOYQNYuw+79DlnO4BskmSZLnQtn7pLiiaBbzkLc8nbEFOnchWq1HZn1U27X4a\nhCn0MbPRkAPhkbN6haB48U5IYy+MwVzroKzo0rmOsWSkL9/enI8fMUe1CMyw0t/+\nn9CbvGV5Soi+Iq6h9XLvHFE2CFrrKXhcdnKaJppxt+LRWH/AHVCLnNYIap/Sz1W7\nktHrtJ8BWiArXTq1WxbZeQmMuQk4UfHS9I+vtakCgYEAzjjFIsNxXFbnwuu94puy\nob1Z+5ZPjatQXlR3tSJQbMpiwt5NCRNJG2OVTJV/QzGV6eHnB70AtK25U0KAVaTz\neKgPqCFb7d2+ZoRBnXB9mosAPkuI3XIyR9mDBZXFJx3bHp4+RRZ5zD3Ls4avef7e\nG6jpLcWFgRwwJnD+1RzoXEUCgYEAydRoRfT0l5pPyCWaVZuttzAFzakUfD8hG6Kw\nUz/oi79cPjiIaETQUCRIECE7nmb36UPgwnPS5I5/fBJypqy482N2E5t5+mkpGUUl\nTrgg1l8i1FZ2C7K0SLlfBk+w0J/A282AvB2VwfPJVz8VWsJ/XguAKspt7EuT9dYW\n+MEleMkCgYAaFSIR6IhQ9ojvpWNp4ulv/YQBBxzevTk4BRTy6vkjGWHuZbF2oWLQ\nvQKoIgxrkjz0zOasmuIY+BQFjNawfmFw9EiuqjF3X2Fyk+28nPq17jjEqEcSQxxK\n7B7fOPcroGITeE5F7LbQ90vpU/KjynGLLAz6Bg6BqvAIHKiOic51xQKBgQDIsxHl\nzwqS3v5LFyl7y81ZBsYelu4qB1TS+FrCziBfJzGBJhJvLU7BAvMuJv30LIyGR9tv\nQmIKqbEYHfgoykU4skUuhkMrwfr+iAXrW6o7wmsOH9RPGauxTbSyv/gh3VqYuKg1\naG4NanFi8vY3RIYHbQRMiPP6L8W4huZdAyRSEQKBgE54frmtb+X+CqV6xZF7yd6E\n8BfCMAOjPKzyP41jWXO6ewVOfrny9jc9mDBZVJhnitT2KUrSMgWxLlLGmihXszwy\nMLv4Agu2eVO10UUb4sagcim+QFYrvJ4U+SWnMgf7DA4EcqAk+QmGTtNOFBBDjlIK\nf9WvY2Lm+hODod0N+8+5\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-38536@tryhackathon.iam.gserviceaccount.com",
  "client_id": "118092460552172352710",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-38536%40tryhackathon.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
firebase_admin.initialize_app(cred, {'databaseURL': 'https://tryhackathon-default-rtdb.firebaseio.com/',
                                     'storageBucket': 'tryhackathon.appspot.com'})
data_ref=db.reference('/aayush2003/json')
ds=storage.bucket()
info = data_ref.get()

def even(n):
    if n%2!=0:
        return False
    else:
        return True

class MatplotlibWidget(Widget):
    def __init__(self, **kwargs):
        super(MatplotlibWidget, self).__init__(**kwargs)
        self.figure, self.ax = plt.subplots()

    def draw(self):
     
        self.ax.plot([1, 2, 3, 4], [10, 5, 20, 15])
        buf = BytesIO()
        self.figure.savefig(buf, format='png')
        buf.seek(0)
        texture = Texture.create(size=(self.figure.get_figwidth() * 100, self.figure.get_figheight() * 100), colorfmt='rgba')
        texture.blit_buffer(buf.getvalue(), colorfmt='rgba', bufferfmt='ubyte')
        self.canvas.ask_update()
        img = Image(texture=texture)
        self.add_widget(img)



class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ColoredBoxLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(58/255, 222/255, 173/255, 1)
            self.rect = Rectangle(size=self.size,pos=self.pos)

# Bind the size and pos properties to update the background color if the size or position changes
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Adjust size_hint to take up the entire width and 10% of the height
        self.size_hint = (1, 0.05)

        # Set pos_hint to place it at the top
        lable=Label(text="Hackathon",color=(1,1,1,1),bold=True,halign='left')
        self.pos_hint = {'top': 1}
        self.add_widget(lable)

    def _update_rect(self, instance, value):
        # Update the background color rectangle when the size or position changes
        self.rect.pos = self.pos
        self.rect.size = self.size


class Main_inp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        master_grid = GridLayout(rows=4, cols=1)
        up_box = ColoredBoxLayout()
        master_grid.add_widget(up_box)
        enter = Label(text="Enter the APP ID to deploy app here", bold=True, color=(0, 0, 0, 1), size_hint=(0.5, 1))
        master_grid.add_widget(enter)
        text_input = TextInput(hint_text='Enter APP ID here', multiline=False, size_hint=(1, None))
        text_input.id = 'appid'
        master_grid.add_widget(text_input)
        deploy = Button(text='DEPLOY!!!', size_hint_y=None, height=100, background_color=(235/255, 235/255, 235/255, 0.5),
                        font_size=22, bold=True, on_press=self.on_submit)
        
        master_grid.add_widget(deploy)
        self.add_widget(master_grid)

    def on_submit(self, instance):
       
        self.manager.current = 'a'
        


class CompleteScreen(Screen):
    def __init__(self,num_graph=1,num_rows=1, num_columns=1,num_stat=1,num_pie=[], **kwargs):
        name = kwargs.pop('screen_name', '')
        super().__init__(**kwargs)
        screen_name = self.name
        master_box=GridLayout(rows=3,cols=1)
        #main_grid=GridLayout(cols=1,rows=3,size_hint_y=1)
        button_grid=GridLayout(cols=2,rows=1,spacing=10,padding=10,size_hint_y=0.2)
        up_box=ColoredBoxLayout()
        
        box_main=BoxLayout(orientation="vertical")
        gridlayout=GridLayout(cols=num_columns,rows=num_rows)
        
        button2= Button(text='<<', size_hint_y=None,height=100,background_color =(235/255, 235/255, 235/255,0.5),font_size=22,bold=True,on_press=self.switch_screen_back)
        button1 = Button(text='>>', size_hint_y=None,height=100,background_color =(235/255, 235/255, 235/255,0.5),font_size=22,bold=True,on_press=self.switch_screen_front)
        #for i in info["screen"]["number"]
        for i in range(num_graph):
            layout = BoxLayout(orientation="vertical")
            
            graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                        x_ticks_major=25, y_ticks_major=1,
                        y_grid_label=True, x_grid_label=True,
                        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
            plot = MeshLinePlot(color=[1, 0, 0, 1])
            graph.tick_color = [0, 0, 0, 1]
            graph.label_color = [0, 0, 0, 1]
            plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
            graph.add_plot(plot)
            layout.add_widget(graph)
            gridlayout.add_widget(layout)
        for j in range(num_stat):
            #label_container = BoxLayout(orientation='vertical', background_color=(0.7, 0.7, 0.7, 1))
            Label1 = Label(text="00", font_size=22, bold=True,color=(0,0,0,1))
            #label_container.add_widget(Label1)
            
            gridlayout.add_widget(Label1)
        box_main.add_widget(gridlayout)
        for k in num_pie:
            storage_ref = storage.bucket().get_blob(k)

            # Download the image as bytes
            image_data = storage_ref.download_as_bytes()

            # Create a BytesIO object to create a CoreImage
            image_stream = BytesIO(image_data)
            
            # Create a Kivy Image widget with the downloaded image data
            kivy_image = Image(texture=CoreImage(image_stream, ext="png").texture)

            gridlayout.add_widget(kivy_image)
    
        button_grid.add_widget(button2)
        button_grid.add_widget(button1)


        #main_grid.add_widget(button_grid)
        master_box.add_widget(up_box)
        master_box.add_widget(box_main)
        master_box.add_widget(button_grid)
        self.add_widget(master_box)

    def switch_screen_front(self, instance):
        curr = self.manager.current
        #print("curr=",curr)
        num=info["screen"]
        l=[i for i in num["number"]]  
        #print(l)
        ind=l.index(curr)
        try:
            tar = l[ind + 1]
            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = tar
            
        except IndexError:
            print("nope")
    def switch_screen_back(self,instance):
        curr = self.manager.current
        #print("curr=",curr)
        num=info["screen"]
        l=[i for i in num["number"]]  
        #print(l)
        ind=l.index(curr)
        try:
            tar = l[ind - 1]
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = tar
            
        except IndexError:
            print("nope")


class MyScreenApp(App):
    def build(self):
        self.manager = ScreenManager()
        appid=Main_inp()
        self.manager.add_widget(appid)
        num = info["screen"]
        screens = num["number"]
        a=[]
        b=[]
        c=[]
        blobs = ds.list_blobs()
        image_names = [blob.name for blob in blobs]
        print(image_names)
        for k in image_names:
            if k.split("-")[1]=='a.png':
                a.append(k)
            elif k.split("-")[1]=='b.png':
                b.append(k)
            elif k.split("-")[1]=='c.png':
                c.append(k)
        l=[i for i in screens]
        #QRCodeReaderScreen1=QRCodeReaderScreen(name="reader")
        #self.manager.add_widget(QRCodeReaderScreen1)
        img=[a,b,c]
        print(img)
        for o in range(0,len(l)):
            i=l[o]
            num_graph=0
            num_rows=0
            num_columns=0
            graph=screens[i]["graph"]
            stat=screens[i]["stat"]
            cols=0
            if even(graph+stat+3)==True:
                num_graph=num_graph+graph 
                cols=stat+graph+3
            elif even(graph+stat+3)==False:
                num_graph=num_graph+graph
                cols=graph+stat+1+3
                
            num_rows=num_rows+cols/2
            num_columns=num_columns+2   
            graph_screen = CompleteScreen(name=i,num_graph=num_graph,num_rows=int(num_rows),num_columns=int(num_columns),num_stat=stat,num_pie=img[o])
            self.manager.add_widget(graph_screen)
            
        Window.size=(400,600)
        Window.clearcolor=(1,1,1,1)
        return self.manager


if __name__ == '__main__':
    MyScreenApp().run()
