import streamlit as st

SIZE_93C86_CEM = 2048
SIZE_28F400_CEM = 524288

pinNameBySize = {
    SIZE_93C86_CEM: "93C86 CEM",
    SIZE_28F400_CEM: "28F400 CEM",
}
pinAddresBySizeMap = {
    SIZE_93C86_CEM: [
        [0x4E3,0x4E1,0x4E5,0x4E0,0x4E2,0x4E4],
    ],
    SIZE_28F400_CEM: [
        [0x4000,0x4001,0x4002,0x4003,0x4004,0x4005],
        [0x6000,0x6001,0x6002,0x6003,0x6004,0x6005],
    ],
}

uploaded_file = st.file_uploader("Choose a file")
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
    
