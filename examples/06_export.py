"""Export a list — CSV (signed URL) and JSON (inline, paginated). Free.

    python examples/06_export.py <list_id>
"""
import sys
import urllib.request

from _common import client

from cleanlist_ai.models import ExportCsvRequest


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python examples/06_export.py <list_id>")
    list_id = sys.argv[1]

    with client() as cl:
        # CSV: returns a short-lived signed URL you can hand to a browser or download.
        signed = cl.export.export_csv(ExportCsvRequest(list_id=list_id))
        print(f"CSV: {signed.row_count} rows, {signed.file_size_bytes} bytes")
        print(f"     download_url (expires {signed.expires_at}): {signed.download_url}")

        # Optionally fetch it:
        # urllib.request.urlretrieve(signed.download_url, "export.csv")

        # JSON: rows come back inline, page by page.
        cursor = None
        count = 0
        while True:
            data = cl.export.export_json(list_id, limit=500, cursor=cursor)
            count += len(data.leads)
            cursor = data.cursor
            if not cursor:
                break
        print(f"JSON: streamed {count} of {data.total} rows.")


if __name__ == "__main__":
    main()
