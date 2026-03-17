## Short: "strings on exotic files"

---

## Text

strings doesn't care about your file extension.

JPEG? If it was edited in Photoshop or GIMP, the software signs its work. One grep — and you've proven the image was tampered with. Forensics 101.

PDF? Someone sent you an "anonymous" document? strings will read out the author's name, the company, the original file path. Anonymous. Sure.

APK? Your favourite app is just a zip file. Unzip it, run strings, grep for Firebase or amazonaws — and you're reading the backend infrastructure. Hardcoded URLs, internal API paths, user data fields. All of it.

strings doesn't care what you called the file.

---

## Display / CLI / Code

```bash
# 1) JPEG — forensic: was this photo manipulated?
strings photo.jpg | grep -i -E "photoshop|gimp|lightroom|adobe"
```

Show output: `Adobe Photoshop 25.0`, `gimp-2.10` — software signature proves the image was edited.

```bash
# 2) PDF — OPSEC failure: "anonymous" document
strings document.pdf | grep -i -E "author|creator|producer|company|users"
```

Show output:
- `Author: John Doe`
- `/Users/johndoe/Documents/internal_report_FINAL2.pdf`
- `Microsoft Word for Office 365`

```bash
# 3) APK — app recon: what's your app hiding?
unzip -p app.apk | strings | grep -i -E "firebase|amazonaws|api\..*\.com"
```

Show output: Firebase project URL, S3 bucket endpoint, internal API base URL.
