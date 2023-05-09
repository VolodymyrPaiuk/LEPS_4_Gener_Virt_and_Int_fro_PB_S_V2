def create_I (New_test):
    # print(len(New_test))
    # створюю інтернал
    Internal = []
    Internal.append(['InternalModuleNumber', 'InternalModuleGroup', 'ModuleNumber', 'OrderType'])
    while_k = 1

    while while_k < len(New_test):
        while_i = 2
        while while_i < len(New_test[while_k]):
            if New_test[while_k][while_i] == '':
                pass
            else:
                Internal_row = []
                Internal_row.append(New_test[while_k][1])
                Internal_row.append(New_test[while_k][0])
                Internal_row.append(New_test[while_k][while_i] + "_" + New_test[while_k][0])
                Internal.append(Internal_row)
            while_i = while_i + 1
        while_k = while_k + 1

    # print(Internal)
    # module.read_record_csv.record(Internal)
    return Internal

def create_V (New_test):
    # створюю віртуал
    Virtual = []
    Virtual.append(['VirtualModuleNumber', 'ModuleNumber', 'OrderType'])
    while_Virt_k = 1
    while while_Virt_k < len(New_test):
        while_Virt_i = 2
        while while_Virt_i < len(New_test[while_Virt_k]):
            if New_test[while_Virt_k][while_Virt_i] == '':
                pass
            else:
                Variant = New_test[while_Virt_k][while_Virt_i].split('_')
                for x in Variant:
                    Virtual_row = []
                    Virtual_row.append(New_test[while_Virt_k][while_Virt_i] + '_' + New_test[while_Virt_k][0])
                    Virtual_row.append(x)
                    Virtual.append(Virtual_row)
            while_Virt_i += 1
        while_Virt_k += 1
    Virtual_Gen = []
    for i in Virtual:
        if i not in Virtual_Gen:
            Virtual_Gen.append(i)
    # print(Virtual_Gen)
    # module.read_record_csv.record(Virtual_Gen)
    return Virtual_Gen