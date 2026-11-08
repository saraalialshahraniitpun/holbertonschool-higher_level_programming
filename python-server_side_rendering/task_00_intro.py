#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    and a list of attendee dictionaries.
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data or 'N/A'
        name = attendee.get("name")
        name = name if name is not None else "N/A"

        event_title = attendee.get("event_title")
        event_title = event_title if event_title is not None else "N/A"

        event_date = attendee.get("event_date")
        event_date = event_date if event_date is not None else "N/A"

        event_location = attendee.get("event_location")
        event_location = event_location if event_location is not None else "N/A"

        content = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location,
        )

        output_filename = "output_{}.txt".format(index)

        # Write processed template to output file
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
