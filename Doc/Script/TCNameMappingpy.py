class TCNameMapping:
  IeSaveAsBtn = Aliases.browser.dlgInternetExplorer.DirectUIHWND.btnSaveAs
  IeDirectUIHWND = Aliases.browser.BrowserWindow.FrameNotificationBar.DirectUIHWND
  IeDwndirectUIHWND = Aliases.browser.BrowserWindowDwn.FrameNotificationBar.DirectUIHWND
  IeDirectUIHWNDSave = Aliases.browser.BrowserWindow.FrameNotificationBar.DirectUIHWND.Save
  IeDirectUIHWNDClose = Aliases.browser.BrowserWindow.FrameNotificationBar.DirectUIHWND.Close
  SaveAsDialog = Aliases.browser.dlgSaveAs
  SaveAsFileNameEditBox = Aliases.browser.dlgSaveAs.DUIViewWndClassName.DirectUIHWND.FloatNotifySink.ComboBox.Edit
  SaveAsSaveBtn = Aliases.browser.dlgSaveAs.btnSave
  #File Upload Google Chrome
  GCOpenFileDialog = Aliases.browser.dlgOpen
  GCFilenameEditBox = Aliases.browser.dlgOpen.ComboBoxEx32
  GCButtonOpen = Aliases.browser.dlgOpen.btnOpen 
  #File Upload IE
  IEOpenFileDialog = Aliases.browser.dlgChooseFileToUpload
  IEFilenameEditBox = Aliases.browser.dlgChooseFileToUpload.ComboBoxEx32
  IEButtonOpen = Aliases.browser.dlgChooseFileToUpload.btnOpen
  
  def __init__(self):
    Log.Message("Initializing TCNameMapping Class")