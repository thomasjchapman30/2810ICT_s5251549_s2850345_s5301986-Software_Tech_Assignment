import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


file_path = 'CrashStatisticsVictoria.csv'
df = pd.read_csv(file_path, parse_dates=['ACCIDENT_DATE'], dayfirst=True)

class Frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 921,498 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel_home = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel_home.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.m_panel_home.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

        bSizer_home = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_home1 = wx.StaticText( self.m_panel_home, wx.ID_ANY, u"Victoria State Accident DataSet", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_home1.Wrap( -1 )

        self.m_staticText_home1.SetFont( wx.Font( 22, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Garamond" ) )

        bSizer_home.Add( self.m_staticText_home1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )

        self.m_staticText_home2 = wx.StaticText( self.m_panel_home, wx.ID_ANY, u"Welcome to our Victoria State Accident DataSet application, \na comprehensive traffic incident analyzer aimed at \nproviding insights and visualizations based on the extensive \nVictoria State Accident dataset. Our application aims to empower \nusers, researchers, and policy-makers by offering detailed, \nuser-friendly, and customizable insights into traffic incidents, \nenabling a deeper understanding of road safety dynamics in Victoria.\n", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_home2.Wrap( -1 )

        self.m_staticText_home2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Javanese Text" ) )

        bSizer_home.Add( self.m_staticText_home2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 50 )


        self.m_panel_home.SetSizer( bSizer_home )
        self.m_panel_home.Layout()
        bSizer_home.Fit( self.m_panel_home )
        self.m_notebook.AddPage( self.m_panel_home, u"Home Page", False )
        self.m_panel_q1 = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q1 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer_q1_inner1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_q1_1 = wx.StaticText( self.m_panel_q1, wx.ID_ANY, u"Time period for accidents", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q1_1.Wrap( -1 )

        bSizer_q1_inner1.Add( self.m_staticText_q1_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )

        self.m_staticText_q1_2 = wx.StaticText( self.m_panel_q1, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q1_2.Wrap( -1 )

        bSizer_q1_inner1.Add( self.m_staticText_q1_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q1_1 = wx.adv.DatePickerCtrl( self.m_panel_q1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q1_inner1.Add( self.m_datePicker_q1_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText_q1 = wx.StaticText( self.m_panel_q1, wx.ID_ANY, u"End Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q1.Wrap( -1 )

        bSizer_q1_inner1.Add( self.m_staticText_q1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q1_2 = wx.adv.DatePickerCtrl( self.m_panel_q1, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q1_inner1.Add( self.m_datePicker_q1_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button_q1 = wx.Button( self.m_panel_q1, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_q1_inner1.Add( self.m_button_q1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 35 )


        bSizer_q1.Add( bSizer_q1_inner1, 1, wx.EXPAND, 5 )

        bSizer_q1_inner2 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid_q1 = wx.grid.Grid( self.m_panel_q1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_q1.CreateGrid( 20, 8 )
        self.m_grid_q1.EnableEditing( True )
        self.m_grid_q1.EnableGridLines( True )
        self.m_grid_q1.EnableDragGridSize( False )
        self.m_grid_q1.SetMargins( 0, 0 )

        # Columns
        self.m_grid_q1.EnableDragColMove( False )
        self.m_grid_q1.EnableDragColSize( True )
        self.m_grid_q1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_q1.EnableDragRowSize( True )
        self.m_grid_q1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_q1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer_q1_inner2.Add( self.m_grid_q1, 0, wx.ALL, 5 )


        bSizer_q1.Add( bSizer_q1_inner2, 3, wx.EXPAND, 5 )


        self.m_panel_q1.SetSizer( bSizer_q1 )
        self.m_panel_q1.Layout()
        bSizer_q1.Fit( self.m_panel_q1 )
        self.m_notebook.AddPage( self.m_panel_q1, u"Selected Period Accidents", False )
        self.m_panel_q2 = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer_q2_inner1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_q2_1 = wx.StaticText( self.m_panel_q2, wx.ID_ANY, u"Hourly Accident Dates", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q2_1.Wrap( -1 )

        bSizer_q2_inner1.Add( self.m_staticText_q2_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )

        self.m_staticText_q2_2 = wx.StaticText( self.m_panel_q2, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q2_2.Wrap( -1 )

        bSizer_q2_inner1.Add( self.m_staticText_q2_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q2_1 = wx.adv.DatePickerCtrl( self.m_panel_q2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q2_inner1.Add( self.m_datePicker_q2_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText_q2_3 = wx.StaticText( self.m_panel_q2, wx.ID_ANY, u"End Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q2_3.Wrap( -1 )

        bSizer_q2_inner1.Add( self.m_staticText_q2_3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q2_2 = wx.adv.DatePickerCtrl( self.m_panel_q2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q2_inner1.Add( self.m_datePicker_q2_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button_q2 = wx.Button( self.m_panel_q2, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_q2_inner1.Add( self.m_button_q2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 35 )


        bSizer_q2.Add( bSizer_q2_inner1, 1, wx.EXPAND, 5 )

        bSizer_q2_inner2 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_q2_graph = wx.Panel( self.m_panel_q2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer1_q2_inner2_inner1 = wx.BoxSizer( wx.VERTICAL )


        self.m_panel_q2_graph.SetSizer( bSizer1_q2_inner2_inner1 )
        self.m_panel_q2_graph.Layout()
        bSizer1_q2_inner2_inner1.Fit( self.m_panel_q2_graph )
        bSizer_q2_inner2.Add( self.m_panel_q2_graph, 2, wx.EXPAND |wx.ALL, 5 )


        bSizer_q2.Add( bSizer_q2_inner2, 3, wx.EXPAND, 5 )


        self.m_panel_q2.SetSizer( bSizer_q2 )
        self.m_panel_q2.Layout()
        bSizer_q2.Fit( self.m_panel_q2 )
        self.m_notebook.AddPage( self.m_panel_q2, u"Hourly Accidents", False )
        self.m_panel_q3 = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer_q3_inner1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_q3_1 = wx.StaticText( self.m_panel_q3, wx.ID_ANY, u"Accident Keyword and Dates", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q3_1.Wrap( -1 )

        bSizer_q3_inner1.Add( self.m_staticText_q3_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )

        self.m_staticText_q3_2 = wx.StaticText( self.m_panel_q3, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q3_2.Wrap( -1 )

        bSizer_q3_inner1.Add( self.m_staticText_q3_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q3_1 = wx.adv.DatePickerCtrl( self.m_panel_q3, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q3_inner1.Add( self.m_datePicker_q3_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText_q3_3 = wx.StaticText( self.m_panel_q3, wx.ID_ANY, u"End Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q3_3.Wrap( -1 )

        bSizer_q3_inner1.Add( self.m_staticText_q3_3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q3_2 = wx.adv.DatePickerCtrl( self.m_panel_q3, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q3_inner1.Add( self.m_datePicker_q3_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText_q3_4 = wx.StaticText( self.m_panel_q3, wx.ID_ANY, u"Accident Keyword", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q3_4.Wrap( -1 )

        bSizer_q3_inner1.Add( self.m_staticText_q3_4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

        self.m_textCtrl_q3 = wx.TextCtrl( self.m_panel_q3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_q3_inner1.Add( self.m_textCtrl_q3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button_q3 = wx.Button( self.m_panel_q3, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_q3_inner1.Add( self.m_button_q3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 35 )


        bSizer_q3.Add( bSizer_q3_inner1, 1, wx.EXPAND, 5 )

        bSizer_q3_inner2 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid_q3 = wx.grid.Grid( self.m_panel_q3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid_q3.CreateGrid( 10, 8 )
        self.m_grid_q3.EnableEditing( True )
        self.m_grid_q3.EnableGridLines( True )
        self.m_grid_q3.EnableDragGridSize( False )
        self.m_grid_q3.SetMargins( 0, 0 )

        # Columns
        self.m_grid_q3.EnableDragColMove( False )
        self.m_grid_q3.EnableDragColSize( True )
        self.m_grid_q3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid_q3.EnableDragRowSize( True )
        self.m_grid_q3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid_q3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer_q3_inner2.Add( self.m_grid_q3, 1, wx.ALL, 5 )


        bSizer_q3.Add( bSizer_q3_inner2, 2, wx.EXPAND, 5 )


        self.m_panel_q3.SetSizer( bSizer_q3 )
        self.m_panel_q3.Layout()
        bSizer_q3.Fit( self.m_panel_q3 )
        self.m_notebook.AddPage( self.m_panel_q3, u"Keyword Accidents", False )
        self.m_panel_q4 = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q4 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer_q4_inner1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_q4_1 = wx.StaticText( self.m_panel_q4, wx.ID_ANY, u"Impact of Alcohol", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q4_1.Wrap( -1 )

        bSizer_q4_inner1.Add( self.m_staticText_q4_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )

        self.m_staticText_q4_2 = wx.StaticText( self.m_panel_q4, wx.ID_ANY, u"Starting Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q4_2.Wrap( -1 )

        bSizer_q4_inner1.Add( self.m_staticText_q4_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q4_1 = wx.adv.DatePickerCtrl( self.m_panel_q4, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q4_inner1.Add( self.m_datePicker_q4_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText_q4_3 = wx.StaticText( self.m_panel_q4, wx.ID_ANY, u"End Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q4_3.Wrap( -1 )

        bSizer_q4_inner1.Add( self.m_staticText_q4_3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_datePicker_q4_2 = wx.adv.DatePickerCtrl( self.m_panel_q4, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
        bSizer_q4_inner1.Add( self.m_datePicker_q4_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_checkBox_q4 = wx.CheckBox( self.m_panel_q4, wx.ID_ANY, u"Alcohol involed", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_q4.SetValue(True)
        bSizer_q4_inner1.Add( self.m_checkBox_q4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )

        self.m_staticText_q4_4 = wx.StaticText( self.m_panel_q4, wx.ID_ANY, u"Select Collision Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q4_4.Wrap( -1 )

        bSizer_q4_inner1.Add( self.m_staticText_q4_4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        m_comboBox_q4Choices = [ u"Collision with vehicle", u"Collision with a fixed object", u"Struck Pedestrian", u"Vehicle overturned (no collision)", u"Struck animal", wx.EmptyString ]
        self.m_comboBox_q4 = wx.ComboBox( self.m_panel_q4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_q4Choices, 0 )
        bSizer_q4_inner1.Add( self.m_comboBox_q4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button_q4 = wx.Button( self.m_panel_q4, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_q4_inner1.Add( self.m_button_q4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 25 )


        bSizer_q4.Add( bSizer_q4_inner1, 1, wx.EXPAND, 5 )

        bSizer_q4_inner2 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_q4_graph = wx.Panel( self.m_panel_q4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q4_inner2_inner1 = wx.BoxSizer( wx.VERTICAL )


        self.m_panel_q4_graph.SetSizer( bSizer_q4_inner2_inner1 )
        self.m_panel_q4_graph.Layout()
        bSizer_q4_inner2_inner1.Fit( self.m_panel_q4_graph )
        bSizer_q4_inner2.Add( self.m_panel_q4_graph, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer_q4.Add( bSizer_q4_inner2, 3, wx.EXPAND, 5 )


        self.m_panel_q4.SetSizer( bSizer_q4 )
        self.m_panel_q4.Layout()
        bSizer_q4.Fit( self.m_panel_q4 )
        self.m_notebook.AddPage( self.m_panel_q4, u"Impact of Alcohol", True )
        self.m_panel_q5 = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q5 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer_q5_inner1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_q5 = wx.StaticText( self.m_panel_q5, wx.ID_ANY, u"Speed in Km/h", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_q5.Wrap( -1 )

        bSizer_q5_inner1.Add( self.m_staticText_q5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        m_choice1Choices = ['40 Km/h','50 Km/h','60 Km/h','70 Km/h','80 Km/h ','90 Km/h ','100 Km/h', '110 Km/h']
        self.m_choice1 = wx.Choice(self.m_panel_q5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer_q5_inner1.Add(self.m_choice1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button_q5 = wx.Button(self.m_panel_q5, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_q5_inner1.Add(self.m_button_q5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel_q5_graph1 = wx.Panel( self.m_panel_q5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q5_inner1.Add( self.m_panel_q5_graph1, 1, wx.EXPAND |wx.ALL, 5 )
        self.m_panel_q5_graph1_sizer = wx.BoxSizer(wx.VERTICAL)
        self.m_panel_q5_graph1.SetSizer(self.m_panel_q5_graph1_sizer)

        bSizer_q5.Add( bSizer_q5_inner1, 1, wx.EXPAND, 5 )

        bSizer_q5_inner2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel_q5_graph2 = wx.Panel( self.m_panel_q5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer_q5_inner2.Add( self.m_panel_q5_graph2, 1, wx.EXPAND |wx.ALL, 5 )
        self.m_panel_q5_graph2_sizer = wx.BoxSizer(wx.VERTICAL)
        self.m_panel_q5_graph2.SetSizer(self.m_panel_q5_graph2_sizer)


        bSizer_q5.Add( bSizer_q5_inner2, 1, wx.EXPAND, 5 )


        self.m_panel_q5.SetSizer( bSizer_q5 )
        self.m_panel_q5.Layout()
        bSizer_q5.Fit( self.m_panel_q5 )
        self.m_notebook.AddPage( self.m_panel_q5, u"Speed related incidents", False )

        bSizer1.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        self.icon = wx.Icon("caricon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        self.m_button_q1.Bind(wx.EVT_BUTTON, self.on_search_q1)
        self.m_button_q2.Bind(wx.EVT_BUTTON, self.on_search_q2)
        self.m_button_q3.Bind(wx.EVT_BUTTON, self.on_search_q3)
        self.m_button_q4.Bind(wx.EVT_BUTTON, self.on_search_q4)
        self.m_button_q5.Bind(wx.EVT_BUTTON, self.on_search_q5)

    def on_search_q1(self, event):
        start_date = self.m_datePicker_q1_1.GetValue().FormatISODate()
        end_date = self.m_datePicker_q1_2.GetValue().FormatISODate()

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        mask = (df['ACCIDENT_DATE'] >= start_date) & (df['ACCIDENT_DATE'] <= end_date)
        filtered_df = df[mask]

        self.update_grid(self.m_grid_q1, filtered_df)

    def update_grid(self, grid, data):
        grid.ClearGrid()
        if grid.GetNumberRows() > 0:
            grid.DeleteRows(0, grid.GetNumberRows(), True)
        if grid.GetNumberCols() > 0:
            grid.DeleteCols(0, grid.GetNumberCols(), True)
        grid.AppendCols(data.shape[1])
        grid.AppendRows(data.shape[0])

        for col, colname in enumerate(data.columns):
            grid.SetColLabelValue(col, colname)
            grid.SetColSize(col, 120)
            for row, value in enumerate(data[colname]):
                grid.SetCellValue(row, col, str(value))

        grid.AutoSizeColumns(False)

    def on_search_q2(self, event):

        start_date = self.m_datePicker_q2_1.GetValue().FormatISODate()
        end_date = self.m_datePicker_q2_2.GetValue().FormatISODate()

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        mask = (pd.to_datetime(df['ACCIDENT_DATE']) >= start_date) & (pd.to_datetime(df['ACCIDENT_DATE']) <= end_date)
        filtered_df = df[mask].copy()

        filtered_df['HOUR'] = pd.to_datetime(filtered_df['ACCIDENT_TIME'], format='%H.%M.%S').dt.hour
        avg_accidents_per_hour = filtered_df.groupby('HOUR').size() / filtered_df['ACCIDENT_DATE'].dt.date.nunique()

        fig, ax = plt.subplots(figsize=(5, 3))
        avg_accidents_per_hour.plot(kind='bar', ax=ax)
        ax.set_title('Average Number of Accidents per Hour')
        ax.set_xlabel('Hour of the Day')
        ax.set_ylabel('Average Number of Accidents')
        ax.set_xticks(range(24))

        if hasattr(self, 'canvas'):
            self.canvas.Destroy()
        self.canvas = FigureCanvas(self.m_panel_q2_graph, -1, fig)
        sizer = self.m_panel_q2_graph.GetSizer()
        if sizer is not None:
            sizer.Add(self.canvas, 1, wx.EXPAND)
            self.m_panel_q2_graph.Layout()

    def on_search_q3(self, event):

        start_date = self.m_datePicker_q3_1.GetValue().FormatISODate()
        end_date = self.m_datePicker_q3_2.GetValue().FormatISODate()
        keyword = self.m_textCtrl_q3.GetValue()

        mask = (
                (df['ACCIDENT_DATE'] >= start_date) &
                (df['ACCIDENT_DATE'] <= end_date) &
                df['ACCIDENT_TYPE'].str.contains(keyword, case=False, na=False)
        )
        results = df[mask]

        self.update_grid(self.m_grid_q3, results)

    def on_search_q4(self, event):
        start_date = self.m_datePicker_q4_1.GetValue().FormatISODate()
        end_date = self.m_datePicker_q4_2.GetValue().FormatISODate()
        is_alcohol_involved = self.m_checkBox_q4.GetValue()
        accident_type = self.m_comboBox_q4.GetValue()

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        filtered_data = df[
            (df['ACCIDENT_DATE'] >= start_date) &
            (df['ACCIDENT_DATE'] <= end_date) &
            (df['ACCIDENT_TYPE'] == accident_type)
            ]
        if is_alcohol_involved:

            filtered_data = filtered_data[filtered_data['ALCOHOLTIME'] == 'Yes']

        accident_counts = filtered_data.groupby('ACCIDENT_DATE').size().reset_index(name='ACCIDENT_COUNT')

        self.generate_graph(accident_counts)

    def generate_graph(self, data):

        panel_width, panel_height = self.m_panel_q4_graph.GetSize()
        fig_width, fig_height = panel_width / 100, panel_height / 100

        date_range = data['ACCIDENT_DATE'].max() - data['ACCIDENT_DATE'].min()
        if date_range > pd.Timedelta('365 days'):
            data = data.set_index('ACCIDENT_DATE').resample('M').sum().reset_index()
            title = 'Monthly Accident Trends Over Time'
        else:
            title = 'Daily Accident Trends Over Time'

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))

        ax.plot(data['ACCIDENT_DATE'], data['ACCIDENT_COUNT'], marker='o', label='Number of Accidents')
        ax.set_title(title)
        ax.set_xlabel('Date', fontsize=8)
        ax.set_ylabel('Number of Accidents', fontsize=8)

        ax.tick_params(axis='x', rotation=0, labelsize=7)
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))

        if hasattr(self, 'canvas'):
            self.canvas.Destroy()

        self.canvas = FigureCanvas(self.m_panel_q4_graph, -1, fig)
        sizer = self.m_panel_q4_graph.GetSizer()
        sizer.Add(self.canvas, 1, wx.EXPAND)
        self.m_panel_q4_graph.Layout()

    def on_search_q5(self, event):
        selected_speed = self.m_choice1.GetString(self.m_choice1.GetSelection())

        df['SPEED_ZONE'] = df['SPEED_ZONE'].astype(str)

        if '40 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '40 km/hr')
        elif '50 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '50 km/hr')
        elif '60 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '60 km/hr')
        elif '70 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '70 km/hr')
        elif '80 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '80 km/hr')
        elif '90 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '90 km/hr')
        elif '100 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '100 km/hr')
        elif '110 Km/h' in selected_speed:
            mask = (df['SPEED_ZONE'] == '110 km/hr')

        filtered_data = df[mask]

        speeding_counts = filtered_data.groupby('ACCIDENT_DATE').size().reset_index(name='ACCIDENT_COUNT')
        speeding_counts['DAY_OF_WEEK'] = pd.to_datetime(speeding_counts['ACCIDENT_DATE']).dt.day_name()

        self.generate_graph_q5(speeding_counts)
        self.generate_injury_graph(filtered_data)
    def generate_graph_q5(self, data):
        panel_width, panel_height = self.m_panel_q5_graph1.GetSize()
        fig_width, fig_height = panel_width / 100, panel_height / 100

        accidents_by_day = data.groupby('DAY_OF_WEEK').agg({'ACCIDENT_COUNT': 'sum'}).reset_index()

        order_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        accidents_by_day['DAY_OF_WEEK'] = pd.Categorical(accidents_by_day['DAY_OF_WEEK'], categories=order_of_days, ordered=True)
        accidents_by_day = accidents_by_day.sort_values('DAY_OF_WEEK')

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))

        ax.bar(accidents_by_day['DAY_OF_WEEK'], accidents_by_day['ACCIDENT_COUNT'], label='Number of Accidents', color=['blue', 'orange', 'yellow', 'green', 'pink', 'blue', 'purple'])
        ax.set_title('Total Speed Related Accidents Per Day of Week')
        ax.set_xlabel('Day of the Week', fontsize=8)
        ax.set_ylabel('Number of Accidents', fontsize=8)

        ax.tick_params(axis='x', rotation=45, labelsize=7)

        if hasattr(self, 'canvas_q5_1'):
            self.canvas_q5_1.Destroy()

        self.canvas_q5_1 = FigureCanvas(self.m_panel_q5_graph1, -1, fig)
        sizer = self.m_panel_q5_graph1.GetSizer()
        sizer.Add(self.canvas_q5_1, 1, wx.EXPAND)
        self.m_panel_q5_graph1.Layout()
        plt.close(fig)
    def generate_injury_graph(self, data):
        panel_width, panel_height = self.m_panel_q5_graph2.GetSize()
        fig_width, fig_height = panel_width / 100, panel_height / 100

        injury_totals = {
            'Fatalities': data['FATALITY'].sum(),
            'Serious Injuries': data['SERIOUSINJURY'].sum(),
            'Other Injuries': data['OTHERINJURY'].sum(),
            'Non-Injured': data['NONINJURED'].sum()
        }

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        ax.bar(injury_totals.keys(), injury_totals.values(), color=['red', 'orange', 'yellow', 'green'])

        ax.set_title('Total Injuries by Severity')
        ax.set_ylabel('Number of Injuries', fontsize=8)
        ax.tick_params(axis='x', rotation=45, labelsize=7)

        for bar in ax.patches:
            ax.annotate(f'{int(bar.get_height())}',
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        ha='center', va='bottom')

        if hasattr(self, 'canvas_q5_2'):
            self.canvas_q5_2.Destroy()

        self.canvas_q5_2 = FigureCanvas(self.m_panel_q5_graph2, -1, fig)
        sizer = self.m_panel_q5_graph2.GetSizer()
        sizer.Add(self.canvas_q5_2, 1, wx.EXPAND)
        self.m_panel_q5_graph2.Layout()
        plt.close(fig)

if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame(None)
    frame.SetTitle("Victorian Accident Analyser")
    frame.SetSize(1600, 900)
    frame.Show(True)
    app.MainLoop()