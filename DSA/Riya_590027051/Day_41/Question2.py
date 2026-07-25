from collections import deque


def office_printer_wars(jobs):
    queue = deque(jobs)

    # Number of jobs remaining from each department
    sales = jobs.count("S")
    marketing = jobs.count("M")

    # Ban counts
    ban_sales = 0
    ban_marketing = 0

    while sales > 0 and marketing > 0:

        current = queue.popleft()

        if current == "S":

            # Sales has already been banned
            if ban_sales > 0:
                ban_sales -= 1
                sales -= 1

            else:
                # Sales bans one Marketing job
                ban_marketing += 1
                queue.append("S")

        else:  # current == "M"

            # Marketing has already been banned
            if ban_marketing > 0:
                ban_marketing -= 1
                marketing -= 1

            else:
                # Marketing bans one Sales job
                ban_sales += 1
                queue.append("M")

    if sales > 0:
        return "Sales"
    else:
        return "Marketing"


# Driver Code
if __name__ == "__main__":

    jobs = "SMM"

    winner = office_printer_wars(jobs)

    print("Winning Department:", winner)