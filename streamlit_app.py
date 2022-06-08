import streamlit as st

SIZE_93C86_CEM = 2048
SIZE_28F400_CEM = 524288

pinNameBySize = {
    SIZE_93C86_CEM: "93C86 CEM",
    SIZE_28F400_CEM: "28F400 CEM",
}
pinAddresBySizeMap = {
    SIZE_93C86_CEM: [
        [1251,1249,1253,1248,1250,1252],
    ],
    SIZE_28F400_CEM: [
        [16384,16385,16386,16387,16388,16389],
        [24576,24577,24578,24579,24580,24581],
    ],
}

uploaded_file = st.file_uploader("Choose a firmware file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    firmwareSize = len(bytes_data);
    st.text("Size of firmware is " + str(len(bytes_data)) + " bytes")

    if firmwareSize not in pinAddresBySizeMap:
        st.text("Given firmware not supported by size")

    found_flag = False
    possible_addresses = pinAddresBySizeMap[firmwareSize]

    for addresses in possible_addresses:
        pin_candidate = []

        for byte_position in addresses:
            pin_candidate.append(hex(bytes_data[byte_position]))
            
        if pin_candidate != ['0xff'] * 6:
            st.text("PIN found in file! " + pinNameBySize[firmwareSize])
            st.text(pin_candidate)
            found_flag = True

    if not found_flag:
        st.text("No PIN found in file")
    
