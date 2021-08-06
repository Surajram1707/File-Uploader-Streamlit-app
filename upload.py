import streamlit as st
import os
st.set_page_config(page_title='File Uploader Streamlit', layout = 'centered', initial_sidebar_state = 'auto')
st.title("FILE UPLOADER")
st.write("** File Uploader **")
image_file = st.file_uploader("Upload A File",type=['png','jpeg','jpg','csv','docx','pdf','pptx','xlsx'])
st.write("** File Details **")
if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    filetype = {image_file.type}
    st.write(file_details)
    st.write("** Uploaded file preview **")
    if filetype == {'image/png'} or filetype == {'image/jpeg'} or filetype == {'image/jpg'}:
	    st.image(image_file)
	    if st.button("Save file"):
		    with open(os.path.join("Dirname",image_file.name),"wb") as f: 
		      f.write(image_file.getbuffer())         
		    st.success("File Saved!")
    else:
      st.write("No Preview Available!")
      if st.button("Save file"):
          with open(os.path.join("Dirname",image_file.name),"wb") as f: 
          	f.write(image_file.getbuffer())         
          st.success("File Saved!")
      
    
    
    
    


