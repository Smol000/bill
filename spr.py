_ft = []
_ft.append(['Виртуальная память. VMware'])
_ft.append(['Виртуальный процессор не ниже 3.0 ГГц','Виртуальный процессор 3.0 ГГц.'])
_ft.append(['Виртуальный жесткий диск SATA'])
_ft.append(['Виртуальный жесткий диск SSD'])
_ft.append(['Виртуальный шлюз NSX T (Large)'])
_ft.append(['Интернет на гарантированной скорости 100 М'])
_ft.append(['публичного IP адреса'])
_ft.append(['Резервное копирование (на базе Veeam), VM','Резервное копирование (на базе Veeam). Vmware'])
_ft.append(['Резервное копирование Vmware на базе Veeam. Дисковое пространство для хранения бэкапов'])
_ft.append(['Предоставление доступа к Windows Server для виртуальной машины <= 4'])
_ft.append(['Объектное хранилище S3. Объем'])
_ft.append(['Объектное хранилище S3. Исходящий трафик'])
_ft.append(['Виртуальный процессор для Kubernetes'])
_ft.append(['Виртуальная память для Kubernetes'])
_ft.append(['Виртуальный жесткий диск для Kubernetes'])
_ft.append(['Менеджмент ноды для Kubernetes'])
_ft.append(['Предоставление безлимитного доступа в Интернет на гарантированной скорости 1000 Мбит/с'])
_ft.append(['Выделенный Вычислительный сервер 48 ядер. 3.0 ГГц. 1536ГБ RAM'])
_ft.append(['Выделенное Блочное устройство хранения 36x7.6TB SSD'])
_ft.append(['Предоставление доступа к Windows Server для виртуальной машины >4 vCPU (за 1 vCPU)'])
_ft.append(['----21----'])
_ft.append(['Виртуальный шлюз NSX T (X-Large)'])
_ft.append(['Предоставление безлимитного доступа в Интернет на гарантированной скорости 5000 Мбит/с'])
_ft.append(['Выделенный сервер Compute.Custom (88 Core. 2048GB RAM)'])
_ft.append(['Выделенный сервер Compute.Custom (40 Core. 768GB RAM)'])
_ft.append(['----26----'])
_ft.append(['Блочное устройство хранения SSD'])
_ft.append(['Выделенный сервер Х2-740 3.0 (Compute.Large)'])
_ft.append(['----29----'])
_ft.append(['----30----'])
_ft.append(['----31----'])
_ft.append(['----32----'])
_ft.append(['----33----'])
def _getid(t):
    for index, item in enumerate(_ft):
        if t.find(item)>=0:  #тут будет ошибка если item имеет тип list, нужна проверка и доп обход
            return index
