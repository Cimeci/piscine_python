import os


def ft_tqdm(lst: range) -> None:
    """ft_tqdm(lst: range) -> None

    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
"""
    start = os.times().elapsed
    total = len(lst)
    done = 0
    blocks = ["", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]

    for element in lst:
        done += 1
        # if element % 20 == 0 or total - done < 20:
        progress = done / total

        elapsed = os.times().elapsed - start
        its_per_sec = done / elapsed if elapsed > 0 else 0.1
        elapsed_str = f"{int(elapsed // 60):02d}:{int(elapsed % 60):02d}"
        if its_per_sec > 0:
            time_remaining = (total - done) / its_per_sec
            remaining_minutes = int(time_remaining // 60)
            remaining_seconds = int(time_remaining % 60)
            remaining_str = f"{remaining_minutes:02d}:{remaining_seconds:02d}"
        else:
            remaining_str = "??:??"

        columns, _ = os.get_terminal_size()

        percentage = f"{progress*100:3.0f}%|"
        counter = f"| {done}/{total}"
        timer = f" [{elapsed_str}<{remaining_str}, {its_per_sec:.2f}it/s]"

        fixed_space = len(percentage + counter + timer)
        bar_width = max(columns - fixed_space, 1)

        filled_length = bar_width * progress
        filled_int = int(filled_length)
        filled_fraction = filled_length - filled_int
        block_index = int(filled_fraction * 8)

        bar = blocks[8] * filled_int
        if filled_int < bar_width:
            bar += blocks[block_index]
        bar += ' ' * (bar_width - filled_int - 1)

        final_text = percentage + bar + counter + timer

        if len(final_text) > columns:
            available_space = columns - len(percentage + bar + counter)
            if available_space >= 10:
                timer = timer[:available_space]
                final_text = percentage + bar + counter + timer
            else:
                final_text = percentage + bar + counter
                final_text = final_text[:columns]

        print(final_text, end="\r")
        yield element
    print()
