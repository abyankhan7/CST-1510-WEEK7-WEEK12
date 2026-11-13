# Name  : ABYAN KHAN
# Lane  :  AI     (delete two)
# Date  : 13 NOVEMBER 2026

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
def parse(raw_line):
    raw_line = raw_line.strip()
    hostname_part, rest = raw_line.split(",", 1)
    hostname = hostname_part.strip().lower()
    data = {"hostname": hostname}
    records = rest.split(",")
    for rec in records:
       key, value = rec.split("=")
       key = key.strip()
       value = float(value.strip())
       data[key] = value
    return data
print(parse("SRV-02,used=120,total=100"))

with open("messy_lines.txt") as file:
    for line in file:
        new_line = parse(line)
        percentage = (int(new_line['used']) / int(new_line['total'])) *100
        if percentage >=100:
            status = "OVER LIMIT"
        elif percentage >=90:
            status = "WARNING"
        else:
            status = "OK"
        print(f"{new_line['hostname']}, {status}")

def parse_line(raw_line): # clean and convert raw line into dictionary
    parts = raw_line.strip().split(",")
    survey = parts[0].strip().title()
    rating = int(parts[1].split("=")[1].strip())
    age = int(parts[2].split("=")[1].strip())
    data = {
        "Survey": survey,
        "Rating": rating,
        "Age": age
    }
    return data

def status_of(rating): # returns the status flagged or ok of the record based on ratings
    if rating < 0 or rating > 5:
        status = "FLAGGED"
    else:
        status = "OK"
    return status




# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

  # replace with your code
rec = []
raw_records = ["  Survey_2026 , rating=4 , age=23  ","SURVEY_2025, RATING=15, AGE=29 ","  SURVEY_2024 , Rating=8 , Age=39   "," Survey_2023, rating=2, age=19","  survey_2022 , RATING=10 , AGE=80  "]
with open("records.txt", "r") as file:
    for line in file:
        new_record = parse_line(line)
        rec.append(new_record)
print(rec)


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

totalrecords = 0
flaggedrecords = 0
for record in raw_records:
        new_record = parse_line(record)
        status = status_of(new_record["Rating"])
        totalrecords = totalrecords + 1
        print(new_record, "|", status)
        if status == "FLAGGED":
            flaggedrecords = flaggedrecords + 1
print("Total records:", totalrecords)
print("Flagged records:", flaggedrecords)
#for raw_record in raw_records:
 #   pass   # replace with your code


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring