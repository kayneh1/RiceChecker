import tkinter as tk
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split


class RiceClassifierApp:
    def __init__(self, master):
        # tkinter window size and title
        self.master = master
        self.master.title("Rice Classifier App")
        self.master.geometry("500x300")
        self.master.resizable(False, False)

        # reading datafile
        self.df = pd.read_excel('D:\school\ST\Rice_Dataset_Commeo_and_Osmancik\Rice_Cammeo_Osmancik_cleaned.xlsx',
                                sheet_name='Rice')

        # setting up column x for independent variables and y for dependant variable class
        self.x = self.df[
            ["Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length", "Eccentricity", "Convex_Area", "Extent"]]
        self.y = self.df["Class"]

        # training the model with test splits
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2)

        # load the most precise algorithm, the SVM model
        self.model = svm.SVC(kernel='linear', C=1.0)
        self.model.fit(self.x_train, self.y_train)

        # creating input labels and fields
        self.area_label = tk.Label(master, text="Area")
        self.area_label.grid(row=0, column=0)
        self.area_var = tk.StringVar()
        self.area_entry = tk.Entry(master, textvariable=self.area_var)
        self.area_entry.grid(row=0, column=1)

        self.perimeter_label = tk.Label(master, text="Perimeter")
        self.perimeter_label.grid(row=1, column=0)
        self.perimeter_var = tk.StringVar()
        self.perimeter_entry = tk.Entry(master, textvariable=self.perimeter_var)
        self.perimeter_entry.grid(row=1, column=1)

        self.majat_label = tk.Label(master, text="Major axis length")
        self.majat_label.grid(row=2, column=0)
        self.majat_var = tk.StringVar()
        self.majat_entry = tk.Entry(master, textvariable=self.majat_var)
        self.majat_entry.grid(row=2, column=1)

        self.minat_label = tk.Label(master, text="Minor axis length")
        self.minat_label.grid(row=3, column=0)
        self.minat_var = tk.StringVar()
        self.minat_entry = tk.Entry(master, textvariable=self.minat_var)
        self.minat_entry.grid(row=3, column=1)

        self.eccen_label = tk.Label(master, text="Eccentricity")
        self.eccen_label.grid(row=4, column=0)
        self.eccen_var = tk.StringVar()
        self.eccen_entry = tk.Entry(master, textvariable=self.eccen_var)
        self.eccen_entry.grid(row=4, column=1)

        self.convex_label = tk.Label(master, text="Convex area")
        self.convex_label.grid(row=5, column=0)
        self.convex_var = tk.StringVar()
        self.convex_entry = tk.Entry(master, textvariable=self.convex_var)
        self.convex_entry.grid(row=5, column=1)

        self.extent_label = tk.Label(master, text="Extent")
        self.extent_label.grid(row=6, column=0)
        self.extent_var = tk.StringVar()
        self.extent_entry = tk.Entry(master, textvariable=self.extent_var)
        self.extent_entry.grid(row=6, column=1)

        # Create the predict button
        self.predict_button = tk.Button(master, text="Predict", command=self.predict)
        self.predict_button.grid(row=7, column=1)

        # Create the output label
        self.output_label = tk.Label(master, text="")
        self.output_label.grid(row=8, column=1)

    # the predict function will predict which class of rice it is
    def predict(self):


        # Get the input values
        area = self.area_var.get()
        perimeter = self.perimeter_var.get()
        majat = self.majat_var.get()
        minat = self.minat_var.get()
        eccen = self.eccen_var.get()
        convex = self.convex_var.get()
        extent = self.extent_var.get()

        # was having issues with no values , without this the code doesn't run
        if area and perimeter and majat and minat and eccen and convex and extent:
            # converting entry fields strings into floats for the machine to understand
            area = float(area)
            perimeter = float(perimeter)
            majat = float(majat)
            minat = float(minat)
            eccen = float(eccen)
            convex = float(convex)
            extent = float(extent)

            # Predict the rice class using the SVM model
            X = [[area, perimeter, majat, minat, eccen, convex, extent]]
            y_pred = self.model.predict(X)

            # Update the output label with the predicted class
            if y_pred == 0:
                self.output_label.config(text="Predicted Class: Cammeo")
            else:
                self.output_label.config(text="Predicted Class: Osmancik")


# this calls an instance of tkinter and our class

root = tk.Tk()

app = RiceClassifierApp(root)

root.mainloop()
