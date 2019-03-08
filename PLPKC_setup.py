import sys
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets
qtCreatorFile = "plkc.ui"# Name of the file here

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size()) #Dimensiones fijas
        self.bottonpred.clicked.connect(self.calculation) #Esto es para ordenar que cuando se presione vaya a calculo

    def calculation(self):

        from sklearn.externals import joblib

        rfc = joblib.load('modelo_entrenado_19.pkl')

        #Data entry

        paste_seq = str(self.pasteseq.toPlainText())

        #Computing
        polarity = {'A':8.1,'C':5.5,'D':13.0,'E':12.3,'F':5.2,
                    'G':9.0,'H':10.4,'I':5.2,'K':11.3,'L':4.9,
                    'M':5.7,'N':11.6,'P':8.0,'Q':10.5,'R':10.5,
                    'S':9.2,'T':8.6,'V':5.9,'W':5.4,'Y':6.2}

        coil = {'A':0.71,'C':1.19,'D':1.21,'E':0.84,'F':0.71,
                    'G':1.52,'H':1.07,'I':0.66,'K':0.99,'L':0.69,
                    'M':0.59,'N':1.37,'P':1.61,'Q':0.87,'R':1.06,
                    'S':1.34,'T':1.08,'V':0.63,'W':0.76,'Y':1.07}

        helix = {'A':1.42,'C':0.70,'D':1.01,'E':1.51,'F':1.13,
                    'G':0.57,'H':1.00,'I':1.08,'K':1.16,'L':1.21,
                    'M':1.45,'N':0.67,'P':0.57,'Q':1.11,'R':0.98,
                    'S':0.77,'T':0.83,'V':1.06,'W':1.08,'Y':0.69}

        kyte_doolittle = {'A':1.80,'C':2.50,'D':-3.50,'E':-3.50,'F':2.80,
                     'G':-0.40,'H':-3.20,'I':4.50,'K':-3.90,'L':3.80,
                     'M':1.90,'N':-3.50,'P':-1.60,'Q':-3.50,'R':-4.50,
                     'S':-0.80,'T':-0.70,'V':4.20,'W':-0.90,'Y':-1.30}

        net_charge = {'A':0,'C':0,'D':-1,'E':-1,'F':0,
                        'G':0,'H':0,'I':0,'K':1,'L':0,
                        'M':0,'N':0,'P':0,'Q':0,'R':1,
                        'S':0,'T':0,'V':0,'W':0,'Y':0}

        net_hydrogen = {'A':0,'C':0,'D':1,'E':1,'F':0,
                        'G':0,'H':1,'I':0,'K':2,'L':0,
                        'M':0,'N':2,'P':0,'Q':2,'R':4,
                        'S':1,'T':1,'V':0,'W':1,'Y':1}

        a_polarity = paste_seq.count("A")*polarity["A"]
        c_polarity = paste_seq.count("C")*polarity["C"]
        d_polarity = paste_seq.count("D")*polarity["D"]
        e_polarity = paste_seq.count("E")*polarity["E"]
        f_polarity = paste_seq.count("F")*polarity["F"]
        g_polarity = paste_seq.count("G")*polarity["G"]
        h_polarity = paste_seq.count("H")*polarity["H"]
        i_polarity = paste_seq.count("I")*polarity["I"]
        k_polarity = paste_seq.count("K")*polarity["K"]
        l_polarity = paste_seq.count("L")*polarity["L"]
        m_polarity = paste_seq.count("M")*polarity["M"]
        n_polarity = paste_seq.count("N")*polarity["N"]
        p_polarity = paste_seq.count("P")*polarity["P"]
        q_polarity = paste_seq.count("Q")*polarity["Q"]
        r_polarity = paste_seq.count("R")*polarity["R"]
        s_polarity = paste_seq.count("S")*polarity["S"]
        t_polarity = paste_seq.count("T")*polarity["T"]
        v_polarity = paste_seq.count("V")*polarity["V"]
        w_polarity = paste_seq.count("W")*polarity["W"]
        y_polarity = paste_seq.count("Y")*polarity["Y"]

        a_coil = paste_seq.count("A")*coil["A"]
        c_coil = paste_seq.count("C")*coil["C"]
        d_coil = paste_seq.count("D")*coil["D"]
        e_coil = paste_seq.count("E")*coil["E"]
        f_coil = paste_seq.count("F")*coil["F"]
        g_coil = paste_seq.count("G")*coil["G"]
        h_coil = paste_seq.count("H")*coil["H"]
        i_coil = paste_seq.count("I")*coil["I"]
        k_coil = paste_seq.count("K")*coil["K"]
        l_coil = paste_seq.count("L")*coil["L"]
        m_coil = paste_seq.count("M")*coil["M"]
        n_coil = paste_seq.count("N")*coil["N"]
        p_coil = paste_seq.count("P")*coil["P"]
        q_coil = paste_seq.count("Q")*coil["Q"]
        r_coil = paste_seq.count("R")*coil["R"]
        s_coil = paste_seq.count("S")*coil["S"]
        t_coil = paste_seq.count("T")*coil["T"]
        v_coil = paste_seq.count("V")*coil["V"]
        w_coil = paste_seq.count("W")*coil["W"]
        y_coil = paste_seq.count("Y")*coil["Y"]

        a_helix = paste_seq.count("A")*helix["A"]
        c_helix = paste_seq.count("C")*helix["C"]
        d_helix = paste_seq.count("D")*helix["D"]
        e_helix = paste_seq.count("E")*helix["E"]
        f_helix = paste_seq.count("F")*helix["F"]
        g_helix = paste_seq.count("G")*helix["G"]
        h_helix = paste_seq.count("H")*helix["H"]
        i_helix = paste_seq.count("I")*helix["I"]
        k_helix = paste_seq.count("K")*helix["K"]
        l_helix = paste_seq.count("L")*helix["L"]
        m_helix = paste_seq.count("M")*helix["M"]
        n_helix = paste_seq.count("N")*helix["N"]
        p_helix = paste_seq.count("P")*helix["P"]
        q_helix = paste_seq.count("Q")*helix["Q"]
        r_helix = paste_seq.count("R")*helix["R"]
        s_helix = paste_seq.count("S")*helix["S"]
        t_helix = paste_seq.count("T")*helix["T"]
        v_helix = paste_seq.count("V")*helix["V"]
        w_helix = paste_seq.count("W")*helix["W"]
        y_helix = paste_seq.count("Y")*helix["Y"]

        a_a = round(paste_seq.count("A")/len(paste_seq+str(0.000001)),3)
        c_c = round(paste_seq.count("C")/len(paste_seq+str(0.000001)),3)
        d_d = round(paste_seq.count("D")/len(paste_seq+str(0.000001)),3)
        e_e = round(paste_seq.count("E")/len(paste_seq+str(0.000001)),3)
        f_f = round(paste_seq.count("F")/len(paste_seq+str(0.000001)),3)
        g_g = round(paste_seq.count("G")/len(paste_seq+str(0.000001)),3)
        h_h = round(paste_seq.count("H")/len(paste_seq+str(0.000001)),3)
        i_i = round(paste_seq.count("I")/len(paste_seq+str(0.000001)),3)
        k_k = round(paste_seq.count("K")/len(paste_seq+str(0.000001)),3)
        l_l = round(paste_seq.count("L")/len(paste_seq+str(0.000001)),3)
        m_m = round(paste_seq.count("M")/len(paste_seq+str(0.000001)),3)
        n_n = round(paste_seq.count("N")/len(paste_seq+str(0.000001)),3)
        p_p = round(paste_seq.count("P")/len(paste_seq+str(0.000001)),3)
        q_q = round(paste_seq.count("Q")/len(paste_seq+str(0.000001)),3)
        r_r = round(paste_seq.count("R")/len(paste_seq+str(0.000001)),3)
        s_s = round(paste_seq.count("S")/len(paste_seq+str(0.000001)),3)
        t_t = round(paste_seq.count("T")/len(paste_seq+str(0.000001)),3)
        v_v = round(paste_seq.count("V")/len(paste_seq+str(0.000001)),3)
        w_w = round(paste_seq.count("W")/len(paste_seq+str(0.000001)),3)
        y_y = round(paste_seq.count("Y")/len(paste_seq+str(0.000001)),3)

        a_kyte = paste_seq.count("A")*kyte_doolittle["A"]
        c_kyte = paste_seq.count("C")*kyte_doolittle["C"]
        d_kyte = paste_seq.count("D")*kyte_doolittle["D"]
        e_kyte = paste_seq.count("E")*kyte_doolittle["E"]
        f_kyte = paste_seq.count("F")*kyte_doolittle["F"]
        g_kyte = paste_seq.count("G")*kyte_doolittle["G"]
        h_kyte = paste_seq.count("H")*kyte_doolittle["H"]
        i_kyte = paste_seq.count("I")*kyte_doolittle["I"]
        k_kyte = paste_seq.count("K")*kyte_doolittle["K"]
        l_kyte = paste_seq.count("L")*kyte_doolittle["L"]
        m_kyte = paste_seq.count("M")*kyte_doolittle["M"]
        n_kyte = paste_seq.count("N")*kyte_doolittle["N"]
        p_kyte = paste_seq.count("P")*kyte_doolittle["P"]
        q_kyte = paste_seq.count("Q")*kyte_doolittle["Q"]
        r_kyte = paste_seq.count("R")*kyte_doolittle["R"]
        s_kyte = paste_seq.count("S")*kyte_doolittle["S"]
        t_kyte = paste_seq.count("T")*kyte_doolittle["T"]
        v_kyte = paste_seq.count("V")*kyte_doolittle["V"]
        w_kyte = paste_seq.count("W")*kyte_doolittle["W"]
        y_kyte = paste_seq.count("Y")*kyte_doolittle["Y"]

        a_charge = paste_seq.count("A")*net_charge["A"]
        c_charge = paste_seq.count("C")*net_charge["C"]
        d_charge = paste_seq.count("D")*net_charge["D"]
        e_charge = paste_seq.count("E")*net_charge["E"]
        f_charge = paste_seq.count("F")*net_charge["F"]
        g_charge = paste_seq.count("G")*net_charge["G"]
        h_charge = paste_seq.count("H")*net_charge["H"]
        i_charge = paste_seq.count("I")*net_charge["I"]
        k_charge = paste_seq.count("K")*net_charge["K"]
        l_charge = paste_seq.count("L")*net_charge["L"]
        m_charge = paste_seq.count("M")*net_charge["M"]
        n_charge = paste_seq.count("N")*net_charge["N"]
        p_charge = paste_seq.count("P")*net_charge["P"]
        q_charge = paste_seq.count("Q")*net_charge["Q"]
        r_charge = paste_seq.count("R")*net_charge["R"]
        s_charge = paste_seq.count("S")*net_charge["S"]
        t_charge = paste_seq.count("T")*net_charge["T"]
        v_charge = paste_seq.count("V")*net_charge["V"]
        w_charge = paste_seq.count("W")*net_charge["W"]
        y_charge = paste_seq.count("Y")*net_charge["Y"]

        a_hydrogen = paste_seq.count("A")*net_hydrogen["A"]
        c_hydrogen = paste_seq.count("C")*net_hydrogen["C"]
        d_hydrogen = paste_seq.count("D")*net_hydrogen["D"]
        e_hydrogen = paste_seq.count("E")*net_hydrogen["E"]
        f_hydrogen = paste_seq.count("F")*net_hydrogen["F"]
        g_hydrogen = paste_seq.count("G")*net_hydrogen["G"]
        h_hydrogen = paste_seq.count("H")*net_hydrogen["H"]
        i_hydrogen = paste_seq.count("I")*net_hydrogen["I"]
        k_hydrogen = paste_seq.count("K")*net_hydrogen["K"]
        l_hydrogen = paste_seq.count("L")*net_hydrogen["L"]
        m_hydrogen = paste_seq.count("M")*net_hydrogen["M"]
        n_hydrogen = paste_seq.count("N")*net_hydrogen["N"]
        p_hydrogen = paste_seq.count("P")*net_hydrogen["P"]
        q_hydrogen = paste_seq.count("Q")*net_hydrogen["Q"]
        r_hydrogen = paste_seq.count("R")*net_hydrogen["R"]
        s_hydrogen = paste_seq.count("S")*net_hydrogen["S"]
        t_hydrogen = paste_seq.count("T")*net_hydrogen["T"]
        v_hydrogen = paste_seq.count("V")*net_hydrogen["V"]
        w_hydrogen = paste_seq.count("W")*net_hydrogen["W"]
        y_hydrogen = paste_seq.count("Y")*net_hydrogen["Y"]

        #PROPERTIES Q-P

        aliphatic = round((i_i + l_l + v_v),3)

        negative_charged = round((d_d + e_e),3)

        total_charged = round((d_d + e_e + k_k + h_h + r_r),3)

        aromatic = round((f_f + h_h + w_w + y_y),3)

        polar = round((d_d + e_e + r_r + k_k + q_q + n_n),3)

        neutral = round((a_a + g_g + h_h + p_p + s_s + t_t + y_y),3)

        hydrophobic = round((c_c + f_f + i_i + l_l + m_m + v_v + w_w),3)

        positive_charged = round((k_k + r_r + h_h),3)

        tiny = round((a_a + c_c + d_d + g_g + s_s + t_t),3)

        small = round((e_e + h_h + i_i + l_l + k_k + m_m + n_n + p_p + q_q + v_v),3)

        large = round((f_f + r_r + w_w + y_y),3)

        #SCALES

        polaritY = round(((a_polarity+c_polarity+d_polarity+e_polarity+f_polarity+g_polarity+h_polarity+i_polarity+k_polarity+l_polarity+m_polarity+n_polarity+p_polarity+q_polarity+r_polarity+s_polarity+t_polarity+v_polarity+w_polarity+y_polarity)/len(paste_seq+str(0.000001))),3)

        coiL = round(((a_coil+c_coil+d_coil+e_coil+f_coil+g_coil+h_coil+i_coil+k_coil+l_coil+m_coil+n_coil+p_coil+q_coil+r_coil+s_coil+t_coil+v_coil+w_coil+y_coil)/len(paste_seq+str(0.000001))),3)

        heliX = round(((a_helix+c_helix+d_helix+e_helix+f_helix+g_helix+h_helix+i_helix+k_helix+l_helix+m_helix+n_helix+p_helix+q_helix+r_helix+s_helix+t_helix+v_helix+w_helix+y_helix)/len(paste_seq+str(0.000001))),3)

        kyleD = round(((a_kyte+c_kyte+d_kyte+e_kyte+f_kyte+g_kyte+h_kyte+i_kyte+k_kyte+l_kyte+m_kyte+n_kyte+p_kyte+q_kyte+r_kyte+s_kyte+t_kyte+v_kyte+w_kyte+y_kyte)/len(paste_seq+str(0.000001))), 3)

        netCharge = a_charge+c_charge+d_charge+e_charge+f_charge+g_charge+h_charge+i_charge+k_charge+l_charge+m_charge+n_charge+p_charge+q_charge+r_charge+s_charge+t_charge+v_charge+w_charge+y_charge

        netH = round((a_hydrogen+c_hydrogen+d_hydrogen+e_hydrogen+f_hydrogen+g_hydrogen+h_hydrogen+i_hydrogen+k_hydrogen+l_hydrogen+m_hydrogen+n_hydrogen+p_hydrogen+q_hydrogen+r_hydrogen+s_hydrogen+t_hydrogen+v_hydrogen+w_hydrogen+y_hydrogen), 3)

        result = "Probable: " + str(rfc.predict([[polaritY,coiL,heliX,netH,netCharge,kyleD,a_a,c_c,d_d,e_e,f_f,g_g,h_h,i_i,k_k,l_l,m_m,n_n,p_p,q_q,r_r,s_s,t_t,v_v,w_w,y_y,tiny,small,large,aliphatic,aromatic,total_charged,negative_charged,positive_charged,polar,neutral,hydrophobic]]))


        self.textpred.setText(str(result))
        self.textpred1.setText("A: " + str(a_a) + " , " + "C: " + str(c_c) + " , " + "D: " + str(d_d) + " , " + "E: " + str(e_e) + " , " + "F: " + str(f_f) + " , " + "E: " + str(e_e) + " , " + "G: " + str(g_g) + " , " + "I: " + str(i_i) + " , " + "K: " + str(k_k) + " , " + "L: " + str(l_l) + " , " + "M: " + str(m_m) + " , " + "N: " + str(n_n) + " , " + "P: " + str(p_p) + " , " + "Q: " + str(q_q) + " , " + "R: " + str(r_r) + " , " + "S: " + str(s_s) + " , " + "T: " + str(t_t) + " , " + "V: " + str(v_v) + " , " + "W: " + str(w_w) + " , " + "Y: " + str(y_y))

        self.textpred2.setText("Aliphatic: " + str(aliphatic) + " , " + " (-)charged: " + str(negative_charged) + " , " + " (+)charged: " + str(positive_charged) + " , " + " Aromatic: " + str(aromatic) + " , " + " Polar: " + str(polar) + " , " + " Neutral: " + str(neutral) + " , " + " Hydrophobic: " + str(hydrophobic) + " , " + " Tiny: " + str(tiny) + " , " + " Small: " + str(small) + " , " + " Large: " + str(large) + " , " + " Kyte-Doolittle index: " + str(kyleD) + " , " + " Net charge: " + str(netCharge) + " , " + " Net hydrogen: " + str(netH) + " , " + " Total charged: " + " , " + str(total_charged) + " , " + " Polarity: " + " , " + str(polaritY) + " , " + " Coil: " + " , " + str(coiL) + " , " + " Helix: " + " , " + str(heliX))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
