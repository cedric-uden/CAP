class CurrentState {
    constructor() {
        this.all_entries = false;
        this.debug_output = false;
    }
}

let state = new CurrentState();

function toggle_state_ALL_ENTRIES() {
    if (state.all_entries) {
        document.getElementById("all_entries_btn").innerHTML = "Alle Einträge";
    } else {
        document.getElementById("all_entries_btn").innerHTML = "Neusten Einträge";
    }
    state.all_entries = !state.all_entries;

    update();
}

function toggle_state_DEBUG_OUTPUT() {
    if (state.debug_output) {
        document.getElementById("full_debug_btn").innerHTML = "Detailierte Ausgabe";
    } else {
        document.getElementById("full_debug_btn").innerHTML = "Einfache Ausgabe";
    }
    state.debug_output = !state.debug_output;

    update();
}


function readFile() {
    let file = "/cap.log";
    let f = new XMLHttpRequest();
    let res = "";
    f.open("GET", file, false);
    f.onreadystatechange = function () {
        if (f.readyState === 4) {
            if (f.status === 200) {
                res = f.responseText;
            }
        }
    }
    f.send(null);
    return res.slice(0, -1);
}

function return_split_on_lines(text) {
    return text.split("\n");
}

function return_split_on_logs(line) {
    return line.split(" - ");
}

function put_array_into_string(text_array) {
    let string = "";
    for (let i in text_array) {
        string += text_array[i] + "\n";
    }
    return string;
}

class LogProps {
    constructor() {
        this.date = true;
        this.uuid = true;
        this.module = true;
        this.func = true;
        this.level = true;
        this.msg = true;
    }
}

class LogLevels {
    constructor() {
        this.dbg = false;
        this.info = true;
        this.warn = false;
        this.error = true;
        this.critical = true;
    }
}

function return_log_line_with_these_characteristics(text_array, log_props) {
    for (let i in text_array) {
        let l = return_split_on_logs(text_array[i]);

        line = "";

        if (log_props.date) line += l[0] + " | ";
        if (log_props.uuid) line += l[1] + " | ";
        if (log_props.module) line += l[2] + " | ";
        if (log_props.func) line += l[3] + " | ";
        if (log_props.level) line += l[4] + " | ";
        if (log_props.msg) line += l[5] + " | ";

        text_array[i] = line.slice(0, -3);
    }
    return text_array;
}

function user_log_output(text_array) {

    let log_props = new LogProps();
    log_props.uuid = false;
    log_props.module = false;
    log_props.func = false;
    return return_log_line_with_these_characteristics(text_array, log_props);

}

function omit_log_levels(text_array, log_levels) {

    let out_array = [];

    for (let i in text_array) {

        if (log_levels.dbg) {
            if (text_array[i].includes(" - DEBUG - ")) {
                out_array.push(text_array[i]);
            }
        }
        if (log_levels.info) {
            if (text_array[i].includes(" - INFO - ")) {
                out_array.push(text_array[i]);
            }
        }
        if (log_levels.warn) {
            if (text_array[i].includes(" - WARNING - ")) {
                out_array.push(text_array[i]);
            }
        }
        if (log_levels.error) {
            if (text_array[i].includes(" - ERROR - ")) {
                out_array.push(text_array[i]);
            }
        }
        if (log_levels.critical) {
            if (text_array[i].includes(" - CRITICAL - ")) {
                out_array.push(text_array[i]);
            }
        }

    }
    return out_array;
}

function prepare_log_levels(text_array) {
    let log_levels = new LogLevels();
    text_array = omit_log_levels(text_array, log_levels);
    return text_array;
}

function reverse_array(text_array) {
    return text_array.reverse();
}

function get_most_recent_uuid(text_array) {
    let text_array_length = text_array.length;
    let last_entry_line = text_array[text_array_length - 1];
    let last_uuid = return_split_on_logs(last_entry_line)[1];
    console.log(last_uuid);
    return last_uuid
}

function get_logs_from_most_recent_uuid(text_array) {
    let out_array = [];
    let last_uuid = get_most_recent_uuid(text_array);
    for (let i in text_array) {
        if (text_array[i].includes(last_uuid)) {
            out_array.push(text_array[i]);
        }
    }
    return out_array;
}

function log_output() {

    let text = readFile();
    let text_array = return_split_on_lines(text);

    if (!state.all_entries) {
        text_array = get_logs_from_most_recent_uuid(text_array);
    }
    text_array = reverse_array(text_array);

    if (!state.debug_output) {
        text_array = prepare_log_levels(text_array);
        text_array = user_log_output(text_array);
    }

    let output = put_array_into_string(text_array);
    document.getElementById("log-div").innerHTML = output;
}


function update() {
    log_output();
}
