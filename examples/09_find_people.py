"""Find people by filters — look up valid values, preview the compiled query, search.

Free: searching spends no credits (credits are spent only when you enrich or save).

    python examples/09_find_people.py
"""
from _common import client

from cleanlist_ai.models import CompileRequest, PeopleSearchCriteria, PeopleSearchRequest


def main() -> None:
    with client() as cl:
        # 1. Look up valid filter values. Fixed-enum fields (seniority, departments, ...)
        #    return a canned list; free-text fields (titles, locations) autocomplete `query`.
        seniority = cl.people_finder.search_filters_people("seniority")
        print("Seniority values:", ", ".join(o.id for o in seniority.options[:8]))

        titles = cl.people_finder.search_filters_people("titles", query="vp sales")
        print("Title suggestions:", ", ".join(o.label for o in titles.options[:5]))

        criteria = PeopleSearchCriteria(
            jobTitlesInclude=["VP of Sales", "Head of Sales"],
            seniority=["Vice President"],
            contactCountries=["USA", "CAN"],
            companySizes=["51-200", "201-500"],
        )

        # 2. Dry run: compile the criteria into the provider filter without searching.
        compiled = cl.people_finder.compile_search(CompileRequest(criteria=criteria))
        print(f"Compiled route: {compiled.route}")
        for warning in compiled.warnings or []:
            print(f"  warning: {warning}")

        # 3. Search. `limit` caps this page; pass `cursor` back for the next one.
        page = cl.people_finder.search_people(PeopleSearchRequest(criteria=criteria, limit=10))
        print(f"{page.total} matches (credits charged: {page.credits_charged})")
        for row in page.results:
            print(f"  - {row.full_name} | {row.title} @ {row.company} | {row.linkedin_url}")

        if page.cursor:
            more = cl.people_finder.search_people(
                PeopleSearchRequest(criteria=criteria, limit=10, cursor=page.cursor)
            )
            print(f"Next page: {len(more.results)} more rows")


if __name__ == "__main__":
    main()
