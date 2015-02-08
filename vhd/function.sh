#!/bin/bash

function _vhd_exec_script() {
    script_file=$(mktemp)
    cat > $script_file
    diskpart /s $(cygpath -am $script_file)
    /bin/rm $script_file
}

function vhd_list_volume() {

    input=$1

    if [ -z "$input" ];then
        echo "USAGE: ${FUNCNAME[0]} [DRIVE_LETTER|all|next]"
        return
    fi

    if [ "$input" = "next" ];then
        echo "list volume" | _vhd_exec_script | tail -n 1 | awk '{ print $2 + 1 }'
    elif [ "$input" = "all" ];then
        echo "list volume" | _vhd_exec_script
    else
        echo "list volume" | _vhd_exec_script |
        awk -v letter=$input '{ if ($3 == toupper(letter)) print $2 }'
    fi

}

function vhd_create_master() {

    vhd_file=$1
    label=$2

    if [ -z "$vhd_file" ];then
        echo "USAGE: ${FUNCNAME[0]} VHD_FILE [LABEL]"
        return
    fi
    if [ -z "$label" ];then
        label=$(basename $vhd_file)
    fi

    vhd_file_win=$(cygpath -aw $vhd_file)

_vhd_exec_script << EOF
create vdisk file="$vhd_file_win" maximum=50000 type=expandable
attach vdisk

rescan
rescan
rescan

create partition primary
format fs=ntfs label=$label quick
attributes volume set nodefaultdriveletter

detach vdisk
EOF

}

function vhd_create_snapshot() {

    vhd_file_master=$1
    vhd_file_snapshot=$2

    if [ ! -f "$vhd_file_master" ];then
        echo "USAGE: ${FUNCNAME[0]} VHD_FILE_MASTER [VHD_FILE_SNAPSHOT]"
        return
    fi
    if [ -z "$vhd_file_snapshot" ];then
        vhd_file_snapshot=$(basename $vhd_file_master)
    fi

    vhd_file_master_win=$(cygpath -aw $vhd_file_master)
    vhd_file_snapshot_win=$(cygpath -aw $vhd_file_snapshot)

_vhd_exec_script << EOF
create vdisk file="$vhd_file_snapshot_win" parent="$vhd_file_master_win"
EOF

}

function vhd_mount() {

    vhd_file=$1
    letter=$2

    if [ ! -f "$vhd_file" -o -z "$letter" ];then
        echo "USAGE: ${FUNCNAME[0]} VHD_FILE DRIVE_LETTER"
        return
    fi

    volume_id=$(vhd_list_volume next)
    vhd_file_win=$(cygpath -aw $vhd_file)

_vhd_exec_script << EOF
select vdisk file="$vhd_file_win"
attach vdisk

rescan
rescan
rescan

select volume $volume_id
assign letter=$letter
EOF

    chown ya:None /cygdrive/${letter}
    chmod 755 /cygdrive/${letter}
}

function vhd_umount() {

    vhd_file=$1
    letter=$2

    if [ ! -f "$vhd_file" -o -z "$letter" ];then
        echo "USAGE: ${FUNCNAME[0]} VHD_FILE DRIVE_LETTER"
        return
    fi

    volume_id=$(vhd_list_volume $letter)
    vhd_file_win=$(cygpath -aw $vhd_file)

_vhd_exec_script << EOF
select volume $volume_id
remove letter=$letter
select vdisk file="$vhd_file_win"
detach vdisk
EOF

}

function vhd_extract() {

    archive_app=$1
    archive_os=$2

    if [ ! -f "$archive_app" -o ! -f "$archive_os" ];then
        echo "USAGE: ${FUNCNAME[0]} ARCHIVE_APP ARCHIVE_OS"
        return
    fi
    if [ ! -d /cygdrive/o -o ! -d /cygdrive/s ];then
        echo "ERROR: mount vhd first"
        return
    fi

    extract_dir=__extract__
    mkdir -p /cygdrive/{o,s}/${extract_dir}

    tar -xf $archive_os -C /cygdrive/o/${extract_dir}
    tar -xf $archive_app -C /cygdrive/s/${extract_dir}

#     7z x -y -oO:/${extract_dir} $(cygpath -am $archive_os) > /dev/null
#     7z x -y -oS:/${extract_dir} $(cygpath -am $archive_app) > /dev/null
}

function _vhd_do_mklink() {

    dir=$1
    link=$2
    letter=$3

    (
        cd $dir
        cmd /c "mklink /d $link $letter:" > /dev/null
    )

    from=$(stat --format=%N ${dir}/${link} | awk -v r="['\`]" '{ p = $1; gsub(r, "", p); print p; }')
    to=$(  stat --format=%N ${dir}/${link} | awk -v r="['\`]" '{ p = $3; gsub(r, "", p); print p; }')
    echo "$from -> $to"
}

function vhd_mklink() {

    link_app=$1
    link_os=$2

    if [ -z "$link_app" -o -z "$link_os" ];then
        echo "USAGE: ${FUNCNAME[0]} LINK_NAME_APP LINK_NAME_OS"
        return
    fi

    rm -f /cygdrive/c/Temp/app/${link_app}
    rm -f /cygdrive/c/Temp/os/${link_os}

    (
        _vhd_do_mklink /cygdrive/c/Temp/app $link_app S
        _vhd_do_mklink /cygdrive/c/Temp/os  $link_os  O
    ) | column -t
}
