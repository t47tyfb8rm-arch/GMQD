from pathlib import Path


TARGET = Path("index.html")
VERSION_TO = "20260729-v1-sort-scroll-guard"


CSS_PATCH = """
        /* github patch: sort scroll guard */
        .sort-list {
            touch-action: pan-y !important;
        }
        .sort-row {
            touch-action: pan-y !important;
        }
        .sort-row.dragging {
            touch-action: none !important;
        }
"""


OLD_START = """    function startSortLongPress(event, id) {
        event.preventDefault();
        event.stopPropagation();
        clearSortDragState();
        if (event.currentTarget?.setPointerCapture && event.pointerId !== undefined) {
            try { event.currentTarget.setPointerCapture(event.pointerId); } catch (error) {}
        }
        sortDragState = {
            id,
            startX: event.clientX,
            startY: event.clientY,
            active: false,
            lastX: event.clientX,
            lastY: event.clientY,
            timer: window.setTimeout(() => {
                activateSortDrag(id);
            }, 160),
        };
        window.addEventListener('pointermove', handleSortPointerMove, { passive: false });
        window.addEventListener('pointerup', finishSortDrag, { once: true });
        window.addEventListener('pointercancel', finishSortDrag, { once: true });
    }
"""


NEW_START = """    function startSortLongPress(event, id) {
        clearSortDragState();
        sortDragState = {
            id,
            startX: event.clientX,
            startY: event.clientY,
            active: false,
            cancelled: false,
            row: event.currentTarget,
            pointerId: event.pointerId,
            lastX: event.clientX,
            lastY: event.clientY,
            timer: window.setTimeout(() => {
                activateSortDrag(id);
            }, 320),
        };
        window.addEventListener('pointermove', handleSortPointerMove, { passive: false });
        window.addEventListener('pointerup', finishSortDrag, { once: true });
        window.addEventListener('pointercancel', finishSortDrag, { once: true });
    }
"""


OLD_ACTIVATE = """    function activateSortDrag(id) {
        if (!sortDragState || String(sortDragState.id) !== String(id) || sortDragState.active) return;
        sortDragState.active = true;
        if (navigator.vibrate) navigator.vibrate(18);
        document.body.classList.add('sort-dragging');
        const x = sortDragState.lastX ?? sortDragState.startX;
        const y = sortDragState.lastY ?? sortDragState.startY;
        renderSortList();
        createSortDragGhost(id, x, y);
    }
"""


NEW_ACTIVATE = """    function activateSortDrag(id) {
        if (!sortDragState || sortDragState.cancelled || String(sortDragState.id) !== String(id) || sortDragState.active) return;
        sortDragState.active = true;
        if (sortDragState.row?.setPointerCapture && sortDragState.pointerId !== undefined) {
            try { sortDragState.row.setPointerCapture(sortDragState.pointerId); } catch (error) {}
        }
        if (navigator.vibrate) navigator.vibrate(18);
        document.body.classList.add('sort-dragging');
        const x = sortDragState.lastX ?? sortDragState.startX;
        const y = sortDragState.lastY ?? sortDragState.startY;
        renderSortList();
        createSortDragGhost(id, x, y);
    }
"""


OLD_MOVE = """    function handleSortPointerMove(event) {
        if (!sortDragState) return;
        sortDragState.lastX = event.clientX;
        sortDragState.lastY = event.clientY;
        if (!sortDragState.active) return;
        event.preventDefault();
        moveSortDragGhost(event.clientX, event.clientY);
        const target = document.elementFromPoint(event.clientX, event.clientY)?.closest('.sort-row');
"""


NEW_MOVE = """    function handleSortPointerMove(event) {
        if (!sortDragState) return;
        sortDragState.lastX = event.clientX;
        sortDragState.lastY = event.clientY;
        const dx = event.clientX - sortDragState.startX;
        const dy = event.clientY - sortDragState.startY;
        if (!sortDragState.active) {
            if (Math.abs(dy) > 8 || Math.abs(dx) > 12) {
                sortDragState.cancelled = true;
                clearSortDragState();
            }
            return;
        }
        event.preventDefault();
        moveSortDragGhost(event.clientX, event.clientY);
        const target = document.elementFromPoint(event.clientX, event.clientY)?.closest('.sort-row');
"""


def replace_once(html: str, old: str, new: str, label: str) -> str:
    if new in html:
        return html
    if old not in html:
        raise SystemExit(f"未找到{label}，未修改。")
    return html.replace(old, new, 1)


def main() -> None:
    html = TARGET.read_text(encoding="utf-8")

    for old_version in (
        "20260729-v1-dark-sort-theme-button",
        "20260728-v1-swipe-tabs-page-slide",
        "20260728-v1-swipe-tabs-drawer-animation",
        "20260728-v1-swipe-tabs-animation-bolder",
        "20260728-v1-swipe-tabs-animation-stronger",
        "20260728-v1-swipe-tabs-animation",
        "20260728-v1-swipe-tabs-strong",
        "20260728-v1-detail-payment-value-right",
        "20260728-v1-detail-note-full-width",
        "20260728-v1-detail-payment-full-width",
        "20260728-v1-detail-payment-spacing",
        "20260728-v1-detail-remove-total",
        "20260728-v1-detail-vertical-photo-light-text",
        "20260728-v1-detail-exact-three-row",
        "20260728-v1-platform-custom-fallback",
        "20260728-v1-compact-image-actions",
        "20260728-v1-form-detail-polish",
    ):
        html = html.replace(old_version, VERSION_TO)

    if "github patch: sort scroll guard" not in html:
        html = html.replace("    </style>", CSS_PATCH + "\n    </style>", 1)

    html = replace_once(html, OLD_START, NEW_START, "排序长按开始逻辑")
    html = replace_once(html, OLD_ACTIVATE, NEW_ACTIVATE, "排序激活逻辑")
    html = replace_once(html, OLD_MOVE, NEW_MOVE, "排序移动逻辑")

    TARGET.write_text(html, encoding="utf-8")
    print("OK: patched index.html to", VERSION_TO)


if __name__ == "__main__":
    main()
